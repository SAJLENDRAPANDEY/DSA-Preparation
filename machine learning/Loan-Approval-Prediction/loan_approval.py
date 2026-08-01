import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\SAJLE\Downloads\Loan_Data.csv")

# print(data.head())
# print(data.isnull().sum())

# print(data.info())
# print(data.describe())
# print(data.shape)

# print(data.isnull().sum())

data['Gender']=data['Gender'].fillna(data['Gender'].mode()[0])
data['Married']=data['Married'].fillna(data['Married'].mode()[0])

data['Dependents'] = data['Dependents'].fillna(data['Dependents'].mode()[0])
data['Self_Employed']=data['Self_Employed'].fillna(data['Self_Employed'].mode()[0])
data['LoanAmount']=data['LoanAmount'].fillna(data['LoanAmount'].median())
data['Loan_Amount_Term']=data['Loan_Amount_Term'].fillna(0)
data['Credit_History']=data['Credit_History'].fillna(0)


# print(data.isnull().sum())

# print(data['Loan_Status'].value_counts()) 
# y=422 and n=192

# EDA
# sns.countplot(x='Loan_Status',data=data)
# plt.show()

# sns.countplot(x='Gender',data=data)
# plt.show()


# label encoding
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

for col in data.select_dtypes(include="object").columns:
    data[col]=le.fit_transform(data[col])

print(data.head())



# step 7

# print(data.columns)

x=data.drop("Loan_Status",axis=1)
y=data['Loan_Status']


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# print(len(X_train))

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)


# print(y_pred)

# Compare different  models

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)

dt.fit(X_train, y_train)

pred = dt.predict(X_test)

print("Decision Tree Accuracy:", accuracy_score(y_test, pred))


from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(random_state=42)

rf.fit(X_train, y_train)

pred = rf.predict(X_test)

print("Random Forest Accuracy:", accuracy_score(y_test, pred))


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

pred = knn.predict(X_test)

print("KNN Accuracy:", accuracy_score(y_test, pred))


models = {
    "Logistic Regression": model.score(X_test, y_test),
    "Decision Tree": dt.score(X_test, y_test),
    "Random Forest": rf.score(X_test, y_test),
    "KNN": knn.score(X_test, y_test)
}

comparison = pd.DataFrame(models.items(),
                          columns=["Model", "Accuracy"])

print(comparison)


import joblib

joblib.dump(rf, "loan_model.pkl")

loaded_model = joblib.load("loan_model.pkl")


sample = X_test.iloc[[0]]

prediction = rf.predict(sample)

print(prediction)




from sklearn.metrics import accuracy_score,confusion_matrix,classification_report



cm=confusion_matrix(y_test,y_pred)
sns.heatmap(cm,
            annot=True,
            fmt="d",
            cmap="Blues")

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))