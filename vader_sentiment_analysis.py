# importing necessary libraries
import warnings
warnings.filterwarnings('ignore')
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask import Flask, render_template, request, url_for

vds = SentimentIntensityAnalyzer()

# initiate flask
app = Flask(__name__)

# create app route for home page
@app.route('/')
def home():
    return render_template('VADER_aws.html')

# create app route for prediction
@app.route('/Predict', methods = ['POST'])
def Predict():
    
    if request.method == 'POST':
        review_entered = request.form['message']
        scores = vds.polarity_scores(review_entered)
        
        neu_scr = round(scores['neu'], 3)
        pos_scr = round(scores['pos'], 3)
        neg_scr = round(scores['neg'], 3)
        
        comp_scr = round(scores['compound'], 3)
        if comp_scr >= 0.05:
            text_sent = 1 # positive
        elif comp_scr > -0.05 and comp_scr < 0.05:
            text_sent = 2 # neutral
        else:
            text_sent = 3 # negative
        
    
    return render_template('VADER_aws.html', sentiment = text_sent,
                            neutral_scr = neu_scr, positive_scr = pos_scr,
                            negative_scr = neg_scr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# if __name__ == '__main__':
#     app.run(debug = False)