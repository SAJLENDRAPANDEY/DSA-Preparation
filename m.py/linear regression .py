import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data=pd.read_excel(r"C:\Users\SAJLE\Downloads\cgpa_package_data.xlsx")
print(data.head(5))
# print(data.isnull().sum())
sns.scatterplot(x="CGPA",y="Package (LPA)",data=data)
# plt.show()

x=data[["CGPA"]]
y=data["Package (LPA)"]
# print(x)

lr=LinearRegression()
X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)
lr.fit(X_train,y_train)
print(lr.score(X_test,y_test)*100)
pre_data=lr.predict(x)
sns.scatterplot(x="CGPA",y="Package (LPA)",data=data,c="blue")
plt.plot(data["CGPA"],pre_data,c="red")
plt.legend(["org data","pre line"])
plt.show()


print(lr.predict([[6.87]]))