#Decision Tree Regression Mode

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


#Fitting the regression Model to the dataset
library(rpart)
regressor = rpart(formula = Salary~.,data = dataset,control = rpart.control((minsplit = 1)))


#Predicting a new result
ypred = predict(regressor, data.frame(Level = 6.5))

#Visualising the Decision Tree Regression Model results   --->non continuos model,hence giving incorrect plot
ggplot() +
  geom_point((aes(x = dataset$Level,y = dataset$Salary)),
             color ='red') + 
  geom_line((aes(x = dataset$Level,y = predict(regressor, newdata = dataset))),
            color ='blue') +
  ggtitle('Truth or Bluff(Decision Tree Regression Model)') +
  xlab('Level') +
  ylab('Salary')


#Visualising the Regression Model results(for higher resolution and smoother curve)
x_grid = seq(min(dataset$Level), max(dataset$Level),0.01)
ggplot() +
  geom_point((aes(x = dataset$Level,y = dataset$Salary)),
             color ='red') + 
  geom_line((aes(x = x_grid,y = predict(regressor, newdata = data.frame(Level = x_grid)))),
            color ='blue') +
  ggtitle('Truth or Bluff(Regression Model)') +
  xlab('Level') +
  ylab('Salary')