import os

from flask import Flask, request
import pickle

app = Flask(__name__)



import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import PorterStemmer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import re
import json
import flask_cors
flask_cors.CORS(app)

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
ps = PorterStemmer()

def preprocess(text):
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    tokenized = word_tokenize(text)
    if type(tokenized) == tuple:
        tokenized = list(tokenized)
    tokenized = [word.lower() for word in tokenized]
    return tokenized

def tokenize(text):
    return word_tokenize(text)

def pos_tagging(text):
    return pos_tag(text)

def extract_keywords(description):
    stop_words = set(stopwords.words('english'))
    tokenized = word_tokenize(description)
    filtered_words = [word.lower() for word in tokenized if word.lower() not in stop_words]
    keywords = []
    for token, tag in nltk.pos_tag(filtered_words):
        if tag in ['NN', 'NNS', 'NNP', 'NNPS'] and not token.isnumeric():
            keywords.append(token)
    return keywords


def jaccard_similarity(course_keywords, user_keywords):
    intersection = []
    for word in course_keywords:
        if word in user_keywords:
            intersection.append(word)
    union = course_keywords +  [word for word in user_keywords if word not in course_keywords]
    
    jaccard_similarity = len(intersection) / len(union)

    return jaccard_similarity


def lda(text):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(text)
    lda = LatentDirichletAllocation(n_components=2)
    lda.fit(X)
    return lda

def rank_courses(similarity_scores):
    return sorted(similarity_scores, reverse=True)

def train_model(X_train, y_train):
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model

def match_courses(courses, user_interests):
    course_similarities = []
    for course in courses:
        # Extract keywords from course description
        course_description = course['description']
        keywords = extract_keywords(course_description)
        # Compute similarity between course keywords and user interests
        similarity = jaccard_similarity(keywords, user_interests)
        # Append course id and similarity score to list
        course_similarities.append({'course_id': course['id'], 'similarity': similarity})
    # Sort courses by similarity
    sorted_courses = sorted(course_similarities, key=lambda x: x['similarity'], reverse=True)
    # Return top 5 courses
    return sorted_courses[:5]

@app.route("/interests")
def hello_world():
   
    interests = request.args.get('str',default = 'Machine Learning')
    # open the file for reading
    with open('courses.pkl', 'rb') as infile:
        courses = pickle.load(infile)
    interests = re.sub(r'[^a-zA-Z ]', '', interests)
    user_interests = interests.lower().split()
    top_courses = match_courses(courses, user_interests)
    
    results = []
  
    for course in top_courses:
        id = course["course_id"]
        name = [item['name'] for item in courses if item['id'] == id][0]
        desc = [item['description'] for item in courses if item['id'] == id][0]
        similarity = course["similarity"]
        results.append({"description": desc, "course_name": name, "similarity": similarity})
    
    if results is not None:    
        return json.dumps(results)
    else :
        return "ERROR CODE 101, Null Pointer"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    
