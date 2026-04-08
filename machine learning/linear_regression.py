from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

x=np.array([[1],[2],[3],[4]])
y=np.array([6,12,18,24])


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=2)

lr=LinearRegression()
lr.fit(X_train,y_train)

# print(lr.predict([[2]]))

print(lr.predict([[5]]))

# plt.scatter(x,y)
# plt.plot(X_test,lr.predict(X_test),color='red')
# plt.show()

# predict using formula 
# m=(lr.coef_)
# b=(lr.intercept_)
# print(m*5+b)