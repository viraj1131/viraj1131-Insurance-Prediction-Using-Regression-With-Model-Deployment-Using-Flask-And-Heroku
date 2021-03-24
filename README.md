# viraj1131-Insurance-Prediction-Using-Regression-With-Model-Deployment-Using-Flask-And-Heroku

<p>Main objective behind creating this project is to learn how to integrate machine learning model with a web app, how to create api for machine learning model, and how to deploy machine learning model on cloud. From machine learning point of view I have created basic regression model which will predcit insurance amount for an individual based on person given characterstics like age,gender,BMI,children, and region where they live. My motive here is to learn how to create a framework or api for machine learning model and deploy it so pardon me if the model is not 100% accurate.</p>


## Link to Web App: https://predicting-insurance-api.herokuapp.com/

<p>I have used data from Kaggle link is : <b>https://www.kaggle.com/mirichoi0218/insurance</b></p>

<p>To learn how to creat web api and deploy model I have refered this youtube video: <b>https://www.youtube.com/watch?v=mrExsjcvF4o&list=PLZoTAELRMXVOAvUbePX1lTdxQR8EY35Z1&index=2</b></p>

## Steps I have followed for creating this project:

1. creating basic regression model and saving it as pickel file
2. creating web app using flask where I take user inputs from webpage and call my prediction model to find predicted value.
3. creating basic webpage using HTML and CSS
4. creating Procfile and rewuirements file which is important for deploying model on heroku platform.
5. creaintg an app on heroku platform and integrating this repository to deploy model which will create a publicly accessible URL.

## Brief description about data:

<p>Machine Learning with R by Brett Lantz is a book that provides an introduction to machine learning using R. As far as I can tell, Packt Publishing does not make its datasets available online unless you buy the book and create a user account which can be a problem if you are checking the book out from the library or borrowing the book from a friend. All of these datasets are in the public domain but simply needed some cleaning up and recoding to match the format in the book.</p>

<b>Brief understanding of each columns:</b>

* age: indicates age of person. 

* sex: indicates gender of person possible values 'male' and 'female'.

* bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height,
    objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9.

* children: Number of children covered by health insurance / Number of dependents.

* smoker: indicates whether person smoke or not possible values 'yes' and 'no'.

* region: Individual residential area in the US, 'northeast', 'southeast', 'southwest', 'northwest'.

* charges: Individual medical costs billed by health insurance.

## Data Acknowledgements:

* The dataset is available on GitHub here https://github.com/stedy/Machine-Learning-with-R-datasets.


