#Decision Tree Regression

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


from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state =0)  #Random state so that we get the same result
regressor.fit(X,Y)
#Create your regressor here

#Predicting New Result
ypred = regressor.predict(np.array([[6.5]]))


#Visualising the Decision Tree Regression results
plt.scatter(X,Y, color = "red")
plt.plot(X,regressor.predict(X),color = "blue")
plt.title('Truth or Bluff(Decision Tree Model)')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()

#Visualising the Decision Tree Regression results(for higher resolution and smoother curve)
X_grid = np.arange(min(X),max(X),0.01)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X,Y, color = "red")
plt.plot(X_grid,regressor.predict(X_grid),color = "blue")
plt.title('Truth or Bluff(Decision Tree Model)')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()

