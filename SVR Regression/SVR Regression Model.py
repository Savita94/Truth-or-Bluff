#SVR

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
Y = dataset.iloc[:,2:3].values

"""#Splitting the dataset into Training and Test 
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,Y, test_seze =0.2,random_state = 0)"""

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X = sc_x.fit_transform(X)
sc_y = StandardScaler()
Y = sc_y.fit_transform(Y)

#Fitting the SVR to the dataset
from sklearn.svm import SVR
regressor = SVR()   #the kernel can be linear,polynommial or gausian(rbf)
regressor.fit(X,Y)

#Create your regressor here

#Predicting New Result
    y_pred = sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([[6.5]]))))

#Visualising the SVR results
plt.scatter(X,Y, color = "red")
plt.plot(X,regressor.predict(X),color = "blue")
plt.title('Truth or Bluff(Regression Model)')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()

#Visualising the SVR results(for higher resolution and smoother curve)
X_grid = np.arange(min(X),max(X),0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X,Y, color = "red")
plt.plot(X_grid,regressor.predict(X_grid),color = "blue")
plt.title('Truth or Bluff(SVR Model)')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()


