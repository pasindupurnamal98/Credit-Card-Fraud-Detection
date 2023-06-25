# Credit-Card-Fraud-Detection
Credit Card Fraud Detection Model 

This repository contains a machine learning model for credit card fraud detection, specifically designed to handle imbalanced data using undersampling techniques. 
The model is trained on a dataset of credit card transactions made by European cardholders in September 2013, where fraud cases represent only a small fraction of the total transactions.

The dataset consists of numerical features obtained through a PCA transformation, including transaction time, transaction amount, and principal components (V1 to V28). 
In order to address the class imbalance issue, undersampling is employed to reduce the number of majority class instances, allowing for better training and prediction of fraudulent transactions.

## Getting started

1. get the code from the repository
```
git clone [https://github.com/pasindupurnamal98/Credit-Card-Fraud-Detection.git]
```
2. [download the dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud) that will be used to train a transaction classifier. Unzip it and put the content (creditcard.csv) under main folder (Credit-Card-Fraud-Detection)

3. install required python packages if previously not installed

4. Finally run on Jupyter Notebook and enjoy 😉
