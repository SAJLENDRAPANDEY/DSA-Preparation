# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# data=pd.read_excel(r"C:\Users\SAJLE\Downloads\multiple_linear_regression_data.xlsx")
# # print(data.head(5))
# # print(data.isnull().sum())

# # sns.pairplot(data=data)
# # plt.show()
# # sns.heatmap(data=data,annot=True)
# # plt.show
# x=data.iloc[:,:-1]
# y=data["Salary"]
# # print(x)
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# # m1x1+m2x2+c
# from sklearn.linear_model import LinearRegression
# lr=LinearRegression()
# lr.fit(X_train,y_train)
# print(lr.score(X_test,y_test)*100)


# # polynomial regression 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_excel(r"C:\Users\SAJLE\Downloads\polynomial_regression_data_extended.xlsx")
print(data.head(5))

# plt.scatter(data["Level"],data["Salary"])
# plt.show()

x=data[["Level"]]
y=data["Salary"]

from sklearn.preprocessing import PolynomialFeatures
pf=PolynomialFeatures(degree=2)
pf.fit(x)
x=pf.transform(x)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=0.2)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,y_train)
print(lr.score(X_test,y_test)*100)
lr=lr.predict(x)


test=pf.transform([[45]])
print(lr.predict(test))
plt.scatter(data["Level"],data["Salary"])
plt.plot(data["Level"],lr,c="red")
plt.show()
