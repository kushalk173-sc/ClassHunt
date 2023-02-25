# ClassHunt

# Inspiration
It was that time of the year again. December called for course registrations, but with such a wide variety of courses that our college offers now, we were bound to be lost. What GenEd classes should we take? What about our major requirements? This is why we build ClassHunt, a website that tailors to your preferences to suggest ideal courses for your college career.

# What it does
ClassHunt is a website that uses Natural Language Processing (NLP) to learn your preferences and thus suggest courses that cater to you. A simple set of words are good enough for our system to find courses that are similar to the input and whose content covers your wants. Courses that are in progress, and those that will be in the following semesters, are scraped from the University of Maryland's Schedule of Classes. This data is then manipulated using NLP techniques such as tokenization, part-of-speech tagging and Jaccard similarity, which helps you know which courses are best for you.

# How we built it
A major chunk of our website lies on the server side, which was built using Python, NLTK, and sci-kit-learn. These allowed us to create the script and perform the main functionality of the website. To scrape data from the internet we used BeautifulSoup4, and to deploy it to the web we used Google Cloud Run. For the client side of the webpage, we used HTML, CSS, and JavaScript, and also used the VerbWire API to send secure messages to the university server.

# Challenges we ran into
Being our first time building a full-stack website, running into difficulties was inevitable. One of the bigger ones was building the UI/UX of the website, with errors, incompatibilities, and issues with plug-ins. Our backend team have also gone through a lot of problems in deploying the server on Google Cloud with docker dependencies, and in building the NLP software, the heart of our website.

# Accomplishments that we're proud of
Despite all the concerns, we were very pleased with ourselves for completing the project. One of the biggest accomplishments for us was bolstering our communication and the ability to work on a project with a team -- just as it would be in the real world. Moreover, we were able to network with experts in this field and form a strong connection by asking them questions. In addition to that, we learned from each other and improved our ability to make the best of the resources around us.

# What's next for Class Hunt
In the near future, we plan to launch our website on our own domain rather than using GitHub pages. The Server side application is very heavy due to the algorithm, and even though we managed to reduce the API call time by a factor of 30, it still has a call time of 30 seconds. Our final goal is to provide a product that looks sleek, works fast, and provides accurate results.

Built With
beautiful-soup
css
docker
flask
google-cloud-run
html5
javascript
nltk
python
scikit-learn
verbwire


Try it out - http://aryan5276.github.io/
Devpost - https://devpost.com/software/project-kyt175wv08bl
