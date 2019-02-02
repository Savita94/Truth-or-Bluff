# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Polynomial Regression

#Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Position_salaries.csv')
X= dataset.iloc[:,1:2].values  #it is always better if x is a matrix and not an array
Y = dataset.iloc[:,2].values

"""#Splitting the dataset into Training and Test 
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,Y, test_seze =0.2,random_state = 0)"""

#Fitting linear regrssion to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

#Fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 5)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly,Y)

#Visualising the linear Regression results
plt.scatter(X,Y, color = "red")
plt.plot(X, lin_reg.predict(X),color = "blue")
plt.title('Truth or Bluff(Linear Regression)')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()

#Visualising the Polynomial Regression results
plt.scatter(X,Y, color = "red")
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)),color = "blue")
plt.title('Truth or Bluff(Polynomial Regression)')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()

#Predicting New Result with Linear Regression
lin_reg.predict(6.5)

#Predicting New Result with Polynomial Regression
lin_reg2.predict(poly_reg.fit_transform(6.5))
