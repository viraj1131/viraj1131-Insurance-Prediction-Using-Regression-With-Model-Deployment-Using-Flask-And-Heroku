#importing required library
from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('prediction_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():

    #Collecting Inputs from the form
    age = request.form['age']
    sex = request.form['sex']
    bmi = request.form['bmi']
    children = request.form['children']
    smoker = request.form['smoker']
    region = request.form['region']

    # Converting categorical values into integer
    if sex == 'male':
        gender = 1
    else:
        gender = 0

    if smoker == 'yes':
        smoke = 1
    else:
        smoke = 0

    if region == 'southeast':
        reg = 2
    elif region == 'northwest':
        reg = 1
    elif region == 'southwest':
        reg = 3
    else:
        reg = 0

    # store the inputs
    features = [age,gender,bmi,children,smoke,reg]

    # convert user inputs into an array for the model
    int_features = [x for x in features]
    final_features = [np.array(int_features)]

    # calling model for prediction
    prediction = model.predict(final_features)

    # storing and rounding of predicted value
    output = round(prediction[0], 2)

    # Priting the predicted value
    return render_template('home.html', prediction_text='$ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
