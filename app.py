import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model_EI = pickle.load(open('Resources/model_weights/model_EI.pkl', 'rb'))
# model_NS = pickle.load(open('Resources/model_weights/model_NS.pkl', 'rb'))
# model_FT = pickle.load(open('Resources/model_weights/model_FT.pkl', 'rb'))
# model_JP = pickle.load(open('Resources/model_weights/model_JP.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    # takes the user text input

    # clean the text with regex

    # vectorize the cleaned text

    # Product the result for four axes
    prediction_EI = model_EI.predict(X_vectorized)
    # prediction_NS = model_NS.predict(X_vectorized)
    # prediction_FT = model_FT.predict(X_vectorized)
    # prediction_JP = model_JP.predict(X_vectorized)

    # convert the prediction result from 1 and 0 to letters
    output_EI = ????
    output_NS = ????
    output_FT = ????
    output_JP = ????

    return render_template('index.html',
        prediction_text='Your personality type is {output_EI}{output_NS}{output_FT}{output_JP}')

# @app.route('/results',methods=['POST'])
# def results():

#     data = request.get_json(force=True)
#     prediction = model_EI.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)