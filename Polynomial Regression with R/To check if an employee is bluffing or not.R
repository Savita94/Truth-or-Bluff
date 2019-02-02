#Polynomial Rgression

#Importing the datasets
dataset = read.csv('Position_salaries.csv')
dataset = dataset[2:3]

#Splitting the dataset into training and test
#install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$DependentVariable, SplitRatio = 0.8)
# training_set = subset(dataset,split == TRUE)
# test_set = subset(dataset,split == FALSE)

#Feature Scaling
#training_set = scale(training_set)
#test_set = scale(test_set)

#Fitting linear regression to the dataset
lin_reg = lm(formula = Salary ~.,data = dataset)

#Fitting polynomial regression to the datset
dataset$Level2 = dataset$Level^2
dataset$Level311 = dataset$Level^3
poly_reg = lm(formula = Salary~.,data = dataset)

#Visualising the Linear Regression results
install.packages("ggplot2")
library(ggplot2)
ggplot() +
  geom_point((aes(x = dataset$Level,y = dataset$Salary)),
        color ='red') + 
  geom_line((aes(x = dataset$Level,y = predict(lin_reg, newdata = dataset))),
color ='blue') +
  ggtitle('Truth or Bluff(Linear Regression)1') +
  xlab('Level') +
  ylab('Salary')



#Visualising the Polynomial Regression results
ggplot() +
  geom_point((aes(x = dataset$Level,y = dataset$Salary)),
             color ='red') + 
  geom_line((aes(x = dataset$Level,y = predict(poly_reg, newdata = dataset))),
            color ='blue') +
  ggtitle('Truth or Bluff(Polynomial Regression)1') +
  xlab('Level') +
  ylab('Salary')

#Predicting a new result with Linear Regress
ypred = predict(lin_reg, data.frame(Level = 6.5))

#Predicting a new result with Polynomial Regression
ypred2 = predict(poly_reg, data.frame(Level = 6.5,Level2 = 6.5^2,Level311 = 6.5^3))
