import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Preprocessing
df = pd.read_csv("Salary_Data.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_val, y_train, y_val = train_test_split(X,y, test_size = 0.2, random_state = 0)

#Linear Regression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_val)

#Visualising Training Set Results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title("Salary vs Experience (Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

#Visualising Validation Set Results
plt.scatter(X_val, y_val, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue') #Regression line in the simple linear regression model results from a unique equation therefore it ends up with same regression line.
plt.title("Salary vs Experience (Validation Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()