# Sentiment Analysis with VADER

VADER stands for ‘Valence Aware Dictionary and sEntiment Reasoner’. (Note: in the spelling ‘sEntiment’, first letter ‘s’ is a small letter and second letter ‘E’ is capital and it is correct). VADER is a lexicon and rule-based sentiment analysis tool. It is used to analyze the sentiment of a text. Lexicon is a list of lexical features (words) that are labeled with positive or negative based on the semantic meaning. Even an unlabelled text data can be labeled with VADER sentiment analyzer.

Please visit the blog [VADER](https://medium.com/analytics-vidhya/sentiment-analysis-with-vader-label-the-unlabeled-data-8dd785225166)

<br><br>
# Sentiment Analysis
- __Sentiment Analysis__ is about analyzing the sentiment of the text ie if the given text is _Positive_ or _Negative_ or even _Neutral_.
- This repository is all about deployed project of the __VADER Sentiment Analysis__ which takes any contextual text as an input and outputs if the user entered text is _Positive_, _Negative_ or _Neutral_ based on the _Compound_ Score condition.
- You can refer to how one can apply condition and leverage the threshold score to lable the text as _Positive_, _Negative_ or _Neutral_ from the blog

<br><br>
### References for VADER:
   - https://pypi.org/project/vaderSentiment/
   - https://www.udemy.com/share/101WNABEYTcVxUQX4=/
   - https://github.com/cjhutto/vaderSentiment#about-the-scoring

<br><br>
# Deployment in AWS EC2 Instance
- This project is deployed in AWS EC2 Instance with _Free Tier_. You can test the performance of the project in the [Deployed Link](http://ec2-3-135-17-217.us-east2.compute.amazonaws.com:8080/)
- _Note: If the [Deployed Link](http://ec2-3-135-17-217.us-east-2.compute.amazonaws.com:8080/) is not working, that means I have stopped the EC2 Instance to not waste the Free Tier_.

<br><br>  
### References for Deployment:
   - https://www.youtube.com/watch?v=oOqqwYI60FI&list=PLZoTAELRMXVOAvUbePX1lTdxQR8EY35Z1&index=4&ab_channel=KrishNaik
   - https://medium.com/analytics-vidhya/sentiment-analysis-with-vader-label-the-unlabeled-data-8dd785225166
