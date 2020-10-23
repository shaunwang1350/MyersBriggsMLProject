import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

model_EI = pickle.load(open('Resources/model_weights/model_EI.pkl', 'rb'))
model_NS = pickle.load(open('Resources/model_weights/model_NS.pkl', 'rb'))
model_FT = pickle.load(open('Resources/model_weights/model_FT.pkl', 'rb'))
model_JP = pickle.load(open('Resources/model_weights/model_JP.pkl', 'rb'))

vectorizer = pickle.load(open('Resources/vectorizer/vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():

    # takes the user text input
    userInput = [request.form['text']]

    # clean the text with regex

    # vectorize the cleaned text

    userInput_Vectorized = vectorizer.transform(userInput)

    # Product the result for four axes
    prediction_EI = model_EI.predict(userInput_Vectorized)
    prediction_NS = model_NS.predict(userInput_Vectorized)
    prediction_FT = model_FT.predict(userInput_Vectorized)
    prediction_JP = model_JP.predict(userInput_Vectorized)

    # convert the prediction result from 1 and 0 to letters
    output_EI = 'E' if prediction_EI == 0 else "I"
    output_NS = 'N' if prediction_NS == 0 else "S"
    output_FT = 'F' if prediction_FT == 0 else "T"
    output_JP = 'J' if prediction_JP == 0 else "P"

    return render_template('index.html',
        prediction_text=f'Your personality type is {output_EI}{output_NS}{output_FT}{output_JP}')

if __name__ == "__main__":
    app.run(debug=True)