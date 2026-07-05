import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split 


from sklearn.ensemble import RandomForestClassifier

data = pd.read_excel(r"C:\Users\SAJLE\Downloads\random_forest_dataset.xlsx")

data=pd.get_dummies(data,columns=['Education_Level','City'],drop_first=False)

x=data.drop("Target",axis=1)
y=data["Target"]

X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=0.2,random_state=42)

model=DecisionTreeClassifier(max_depth=3)

model.fit(X_train,y_train)
y_pred=model.predict(X_test)

model2=RandomForestClassifier(n_estimators=100,random_state=42)
model2.fit(X_train,y_train)

y_pred2=model2.predict(X_test)







plt.figure(figsize=(10,8))
plot_tree(model,feature_names=x.columns,class_names=["Yes","No"])
# plt.show()


# accuracy
from sklearn.metrics import accuracy_score,confusion_matrix
print("\n Accuracy Score of Decision Tree is :",accuracy_score(y_test,y_pred))

print("\n Accuracy Score of Random Forest is :",accuracy_score(y_test,y_pred2))

print("\nDecision Tree Confusion Matrix:\n", confusion_matrix(y_test,y_pred))
print("\nRandom Forest Confusion Matrix:\n", confusion_matrix(y_test,y_pred2))

# print(y_pred)