from sklearn.linear_model import LinearRegression
import numpy as np

x=np.array([[1],[2],[3],[4]])
y=np.array([6,12,18,24])
lr=LinearRegression()
lr.fit(x,y)
print(lr.predict([[5]]))