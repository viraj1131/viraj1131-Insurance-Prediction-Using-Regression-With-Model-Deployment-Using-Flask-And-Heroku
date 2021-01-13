# importing required library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle


# Reading .csv file and loading into variable
data = pd.read_csv('insurance.csv')

# importing library for converting categorical feature into numeric
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

# converting categorical feature into numeric
data['sex'] = le.fit_transform(data['sex'])
data['smoker'] = le.fit_transform(data['smoker'])
data['region'] = le.fit_transform(data['region'])



# storing data independent and dependent variables
X = data.drop('charges',axis=1)
#print(X.head(10))
y = data['charges']

# spiliting data into training and test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=222)

# Builind the model
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(max_features=4,max_depth=3)

# fitting our model
regressor.fit(X_train, y_train)

# predicting using build model
y_pred = regressor.predict(X_test)
#print('model predicted values:',y_pred[:10])

# Check Accuracy
print("Training set score: {:.4f}".format(regressor.score(X_train, y_train)))
print("Test set score: {:.4f}".format(regressor.score(X_test, y_test)))

# Saving model to disk
pickle.dump(regressor, open('prediction_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('prediction_model.pkl','rb'))
print(model.predict([[25,0,52.68,4,1,0]]))

