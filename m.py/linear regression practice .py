# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np 
# data=pd.read_excel(r"C:\Users\SAJLE\Downloads\age_experience_salary_high_accuracy.xlsx")
# print(data.head(5))
# x=data.iloc[:,:-1]
# y=data["Salary"]

# plt.scatter(data["Age"],data["Salary"])
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.title("age vs salary")
# plt.show()
# # print(x)

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# lr=LinearRegression()
# X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=0.2,)
# lr.fit(X_train,y_train)
# print(lr.score(X_test,y_test)*100)
# new_data = np.array([[41, 9]])
# print(lr.predict(new_data)[0])


#   Question 2   ---> "C:\Users\SAJLE\Downloads\house_prices.xlsx" 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_excel(r"C:\Users\SAJLE\Downloads\house_prices.xlsx")
print(data.head(5))
x=data.iloc[:,:-1]
y=data["Price (k$)"]
# print(x)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=0.2)
lr.fit(X_train,y_train)
print(lr.score(X_test,y_test)*100)
data=[[2500,3,10]]
print(lr.predict(data))


# question  3 --->  