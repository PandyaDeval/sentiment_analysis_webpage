#

# Sentiment Analysis

#

**Tools and Technology Used**

#

**Tools**

- [**Django**](https://www.djangoproject.com/) **-** Django is a free and open-source web framework, written in Python, which follows the model-view-template architectural pattern. It is maintained by the Django Software Foundation.

- [**PyCharm IDE**](https://www.jetbrains.com/pycharm/) **-** PyCharm is an integrated development environment used in computer programming, specifically for the Python language. It is developed by the Czech company JetBrains.

**Technology**

- [**HTML**](https://html.com/) **-** Hypertext Markup Language is the standard markup language for creating web pages and web applications.

- [**CSS**](https://html.com/) **-** Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language like HTML.

- [**Python**](https://www.python.org/) **-** Python is an interpreted high-level programming language for general-purpose programming.



# Introduction

#

Sentiment analysis is extremely useful in social media monitoring as it allows us to gain an overview of the wider public opinion behind certain topics. The applications of sentiment analysis are broad and powerful. The ability to extract insights from social data is a practice that is being widely adopted by organizations across the world. Shifts in sentiment on social media have been shown to correlate with shifts in the stock market.

**ML Part (Python)**

**Components:**

1. [**NLTK**](https://www.nltk.org/) **:** The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language.

1. [**Pandas**](https://pandas.pydata.org/) **:** pandas is a software library written for the Python programming language for data manipulation and analysis.

1. [Dataset](https://docs.google.com/file/d/0B04GJPshIjmPRnZManQwWEdTZjg/edit) of 16,00,000 tweets.

**Description:**

- Training data is imported from the dataset. A list containing tweets and their respective polarities(Sentiment) is formed.
- The text in all tweets is filtered by converting into lowercase and removing all unnecessary punctuations and stopwords (Like &#39;This&#39;,&#39;That&#39;,etc) which play no part in sentiment analysis. Further website urls are also stripped.
- Features are extracted from filtered tweets and the classifier is trained using the training set formed.
- The classifier used is [Naïve Bayes Classifier](https://www.analyticsvidhya.com/blog/2017/09/naive-bayes-explained/) which is based on [Bayes Probability Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem). It returns a probabilities of all possible outcomes or it gives the outcome with highest probability.
- The test accuracy achieved by training a model with a training set of just 20,000 tweets was about 75%.

**Web Part**

**Description:**

- The main problem with the classifier model created earlier was it could not be saved anywhere. Once the terminal containing the trained classifier was closed, it had to be trained again in order to be used again which is too much time consuming.
- This was solved by integrating it into a webpage using the Django framework.
- Once the classifier is trained, the webpage is started. In order to classify a tweet, the user simply has to enter the text in the text box provided and click on submit and the classifier classifies the tweet into either positive or negative.
- This saves the time and effort required to train the classifier several times.