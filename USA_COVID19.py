import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import Ridge
import datetime as dt
import Data as d
import os

def bayesian_prediction(state, days): # takes in argument for the number of days in future that theres going to be a increase
    d.update()
    pathname = d.find_file(state)
    dataset = pd.read_csv(pathname)
    dataset['date'] = pd.to_datetime(dataset['date'])
    dataset['date_f'] = (dataset['date'] - dataset['date'].min())  / np.timedelta64(1,'D')

    X = dataset[['date_f']]
    y = dataset[['cases']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

    regressor = BayesianRidge()
    regressor.fit(X_train, y_train)
    X_prediction_array = X[-days:] # sample in the next 5 days
    y_pred = regressor.predict(X_prediction_array)
    return 'Using the Bayesian Model: In the next {} days in {}, these will be the positive cases {}'.format(days, state, y_pred)

def linear_prediction(state, days):
    d.update()
    pathname = d.find_file(state)
    dataset = pd.read_csv(pathname)
    dataset['date'] = pd.to_datetime(dataset['date'])
    dataset['date_f'] = (dataset['date'] - dataset['date'].min())  / np.timedelta64(1,'D')

    X = dataset[['date_f']]
    y = dataset[['cases']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    X_prediction_array = X[-days:] # sample in the next 5 days
    y_pred = regressor.predict(X_prediction_array)
    return 'Using the Linear Regression Model: In the next {} days in {}, these will be the positive cases {}'.format(days, state, y_pred)

def ridge_prediction(state, days): # takes in argument for the number of days in future that theres going to be a increase
    d.update()
    pathname = d.find_file(state)
    dataset = pd.read_csv(pathname)
    dataset['date'] = pd.to_datetime(dataset['date'])
    dataset['date_f'] = (dataset['date'] - dataset['date'].min())  / np.timedelta64(1,'D')

    X = dataset[['date_f']]
    y = dataset[['cases']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

    regressor = Ridge()
    regressor.fit(X_train, y_train)
    X_prediction_array = X[-days:] # sample in the next 5 days
    y_pred = regressor.predict(X_prediction_array)
    return 'Using the Ridge Model: In the next {} days in {}, these will be the positive cases {}'.format(days, state, y_pred)

def get_rate_of_change(state): # takes in argument for the number of days in future that theres going to be a increase
    d.update()
    pathname = d.find_file(state)
    dataset = pd.read_csv(pathname)
    dataset['date'] = pd.to_datetime(dataset['date'])
    dataset['date_f'] = (dataset['date'] - dataset['date'].min())  / np.timedelta64(1,'D')

    X = dataset[['date_f']]
    y = dataset[['cases']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

    regressor = BayesianRidge() # most accurate model prediction
    regressor.fit(X_train, y_train)
    return 'In {} the COVID-19 cases are increasing by {} daily'.format(state, regressor.intercept_)

def positive_case_update(state): # initials of the state you want
    d.update()
    pathname = d.find_file(state)
    dataset = pd.read_csv(pathname)
    latest_cases = dataset.iloc[-1] # dataset.iloc[] is a dataframe object that contains the columns of the csv in this case (date, cases)
    return '{} positive cases on {}'.format(latest_cases.cases, latest_cases.date)

def train_test_graphs(): # linear regression model => should i make more?
    d.update()
    dataset = pd.read_csv('NJ_Data.csv')
    dataset['date'] = pd.to_datetime(dataset['date'])
    dataset['date_f'] = (dataset['date'] - dataset['date'].min())  / np.timedelta64(1,'D')

    X = dataset[['date_f']]
    y = dataset[['cases']]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=1/3, random_state=0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    '''
    Lets split the data into a training set and test set which:
        1. the training set will help train the data
        2. the test set will run test to test accuracy
        3. using the combination of the two will help make predictions based on the linear regression line created 
    '''

    # Training Set
    viz_train = plt
    viz_train.scatter(X_train, y_train, color='red')
    viz_train.plot(X_train, regressor.predict(X_train), color='blue')
    viz_train.title('Positive Cases (Training set)')
    viz_train.xlabel('Date')
    viz_train.ylabel('Case')
    viz_train.show()

    # Test Set
    viz_test = plt
    viz_test.scatter(X_test, y_test, color='red')
    viz_test.plot(X_train, regressor.predict(X_train), color='blue')
    viz_test.title('Positive Cases (Test set)')
    viz_test.xlabel('Date')
    viz_test.ylabel('Case')
    viz_test.show()


if __name__ == "__main__":
    num = cases_prediction('HI', 5)
    print(num)
    

