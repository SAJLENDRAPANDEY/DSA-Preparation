import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_excel(r"C:\Users\SAJLE\Downloads\cgpa_score_placed_dataset.xlsx")
# print(data.head(5))
x=data.iloc[:,:-1]
y=data["Placed"]
# print(x)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=20)
lr=LogisticRegression()
lr.fit(X_train,y_train)
print(lr.score(X_test,y_test)*100)

from sklearn.metrics import confusion_matrix,recall_score,precision_score,f1_score
cf=confusion_matrix(y_test,lr.predict(X_test))

print(cf)

sns.heatmap(cf,annot=True)
# plt.show()

print(precision_score(y_test,lr.predict(X_test))*100)


print(recall_score(y_test,lr.predict(X_test))*100)

print()