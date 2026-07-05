import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


data=pd.read_excel(r"C:\Users\SAJLE\Downloads\logistic_regression_dataset.xlsx")

x=data[['Age','Salary']]
y=data['Purchased']



X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=2)

# print(len(X_train))


lr=LogisticRegression()
lr.fit(X_train,y_train)

# print(lr.predict(X_test))

# new dataset prediction user ipnput
age=int(input("Enter age: "))
salary=int(input("Enter salary: "))

x_new=pd.DataFrame({
    'Age':[age],
    'Salary':[salary]
})

predictions=lr.predict(x_new)
if predictions[0]==1:
    print("User will purchase ! ")
else:
    print("User not purchase !")




# print(x)

# print(data)


# check score of model
print("Model Accuracy:", lr.score(X_test, y_test))

# create a plot 
# sns.pairplot(data[['Age','Salary','Purchased']],hue='Purchased')
# plt.show()