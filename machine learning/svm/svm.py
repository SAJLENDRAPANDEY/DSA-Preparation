from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel(r"C:\Users\SAJLE\Downloads\random_forest_dataset.xlsx")



data=pd.get_dummies(data,columns=["Education_Level","City"],drop_first=True)

# print(data)

x=data.drop("Target",axis=1)
y=data["Target"]


X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)

scalor=StandardScaler()
X_train=scalor.fit_transform(X_train)
X_test=scalor.transform(X_test)

model=SVC(class_weight='balanced',kernel='linear')
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

from sklearn.metrics import accuracy_score,classification_report

print("Accuracy Score :",accuracy_score(y_test,y_pred))
print("Classification Report :",classification_report(y_test,y_pred))


# print(y_pred)


# print(x)