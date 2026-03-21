import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data=pd.read_excel(r"C:\Users\SAJLE\Downloads\cgpa_score_placed_dataset.xlsx")
print(data.head(5))

x=data.iloc[:,:-1]
y=data["Placed"]
plt.scatter(x="CGPA",y="Score",data=data,hue="Placed")
plt.show()

X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB

gb=GaussianNB()
gb.fit(X_train,y_train)
print(gb.score(X_test,y_test))

# similar test all model accuracy 
