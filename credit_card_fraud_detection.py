# -*- coding: utf-8 -*-
"""credit card fraud detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mQGniwF4NAyfNEvedtdltzHnTzUT_OIM

Importing Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd drive/MyDrive/ML_projects/Credit\ Card\ Fraud\ Detection

# Commented out IPython magic to ensure Python compatibility.
# %ls

credit_card_data = pd.read_csv('creditcard.csv')

credit_card_data.head()

credit_card_data.tail()

#dataset infromation
credit_card_data.info()

#checking the numbe of missing values in each column
credit_card_data.isnull().sum()

#distribution of legit and fraud trasactions
credit_card_data['Class'].value_counts()

"""This Dataset is highly unbalanced

0 --> Normal Transaction
1 --> fraduelent transactions

"""

#separating the data for analysis
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

print(legit.shape)
print(fraud.shape)

#statistical measures of the data
legit.Amount.describe()

fraud.Amount.describe()

#compare the values for both transactions
credit_card_data.groupby('Class').mean()

"""Under - Sampling

Build a sample dataset containing similar distribution of normal transactions and fradulent transactions

Number of Fraudulent Transactions -> 492


"""

legit_sample=legit.sample(n=492)

"""Conctenating two DataFrames"""

new_dataset = pd.concat([legit_sample,fraud],axis = 0)

new_dataset.head()

new_dataset.tail()

new_dataset['Class'].value_counts()

new_dataset.groupby('Class').mean()

"""Splitting the data into Features and Targets"""

X = new_dataset.drop(columns='Class',axis=1)
Y =  new_dataset['Class']

print(X)

print(Y)

"""Split the data into Training data and Testing Data"""

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

"""Model Training

Logistic Regression
"""

model = LogisticRegression()

#training the Logistic Regression model with training data
model.fit(X_train,Y_train)

"""Model Evaluation

Accuracy Score
"""

#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print('Accuracy on training Data',training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print('Accuracy on training Data',test_data_accuracy)

# Manually input the sample data
sample_data = [[0,-1.359807134, -0.072781173, 2.536346738, 1.378155224, -0.33832077, 0.462387778, 0.239598554, 0.098697901, 0.36378697, 0.090794172, -0.551599533, -0.617800856, -0.991389847, -0.311169354, 1.468176972, -0.470400525, 0.207971242, 0.02579058, 0.40399296, 0.251412098, -0.018306778, 0.277837576, -0.11047391, 0.066928075, 0.128539358, -0.189114844, 0.133558377, -0.021053053, 149.62]]

# Make predictions on the sample data
predictions = model.predict(sample_data)

# Print the predicted class
if predictions[0] == 0:
    print("The model predicts the transaction as normal.")
else:
    print("The model predicts the transaction as fraudulent.")