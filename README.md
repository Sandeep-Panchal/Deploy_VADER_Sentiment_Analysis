<center><h1>Sentiment Analysis with VADER</h1>

VADER stands for ‘Valence Aware Dictionary and sEntiment Reasoner’. (Note: in the spelling ‘sEntiment’, first letter ‘s’ is a small letter and second letter ‘E’ is capital and it is correct). VADER is a lexicon and rule-based sentiment analysis tool. It is used to analyze the sentiment of a text. Lexicon is a list of lexical features (words) that are labeled with positive or negative based on the semantic meaning. Even an unlabelled text data can be labeled with VADER sentiment analyzer.

Please visit the blog on [VADER](https://medium.com/analytics-vidhya/sentiment-analysis-with-vader-label-the-unlabeled-data-8dd785225166)

<h1>Sentiment Analysis</h1>
**Sentiment Analysis** is about analyzing the sentiment of the text ie if the given text is *Positive* or *Negative* or even *Neutral*.
This repository is all about deployed project of the **VADER Sentiment Analysis** which takes any contextual text as an input and outputs if the user entered text is *Positive*, *Negative* or *Neutral* based on the *Compound* Score condition.
You can refer to how one can apply condition and leverage the threshold score to lable the text as *Positive*, *Negative* or *Neutral* from the blog [VADER](https://medium.com/analytics-vidhya/sentiment-analysis-with-vader-label-the-unlabeled-data-8dd785225166)

* References for VADER:
  * https://pypi.org/project/vaderSentiment/
  * https://www.udemy.com/share/101WNABEYTcVxUQX4=/
  * https://github.com/cjhutto/vaderSentiment#about-the-scoring

<h1>Deployment in AWS EC2 Instance</h1>
This project is deployed in AWS EC2 Instance with *Free Tier*. You can test the performance of the project in the [Deployed Link](http://ec2-3-135-17-217.us-east-2.compute.amazonaws.com:8080/)
*Note: If the [Deployed Link](http://ec2-3-135-17-217.us-east-2.compute.amazonaws.com:8080/) is not working, that means I have stopped the EC2 Instance to not waste the *Free Tier*.

* References for Deployment:
  * https://www.youtube.com/watch?v=oOqqwYI60FI&list=PLZoTAELRMXVOAvUbePX1lTdxQR8EY35Z1&index=4&ab_channel=KrishNaik
  * https://medium.com/analytics-vidhya/sentiment-analysis-with-vader-label-the-unlabeled-data-8dd785225166
