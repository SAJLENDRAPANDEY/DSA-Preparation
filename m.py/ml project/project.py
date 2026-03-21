import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_excel(r"C:\yash_important data\student_performance_dataset new.xlsx")
print(data.head(5))
data['Result'] = data['Result'].map({'Fail': 0, 'Pass': 1})
x=data[["Hours_Study" , "Attendance" , "CGPA" , "Test_Score"]]
y=data["Result"]


print(data.isnull().sum())

#  1  Regression Models   

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

print(x)

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

lr=LinearRegression()
lr.fit(X_train,y_train)

print(lr.score(X_test,y_test)*100)

print(lr.predict([[1,96,5.64,90]]))

print("Coefficients:", lr.coef_)
print("Intercept:",lr.intercept_)


next step error check krna h 

from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

y_pred=lr.predict(X_test)

print("MSE",mean_squared_error(y_test,y_pred))
# print("RMSE",mean_squared_error(y_test,y_pred,squared=True))
print("MAE",mean_squared_error(y_test,y_pred))
print("r2_score",r2_score(y_test,y_pred))



# 2  ---> Classification Models

# Predict whether a student will pass/fail using Logistic Regression.

# Use Confusion Matrix to evaluate model performance.

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()

data = data.dropna()

x=data[["Hours_Study" , "Attendance" , "CGPA" , "Final_Score"]]
y=data["Result"]


print(data[['Result']])


X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
x=lr.fit(X_train,y_train)
print(lr.predict([[3,97,6.3,50]]))

y_pred=lr.predict(X_test)


# confusion matrix

from sklearn.metrics import confusion_matrix,recall_score,precision_score,f1_score,classification_report

cm=confusion_matrix(y_test,y_pred)
print("Confusion matrix",cm)

print("\nClassification Report:\n", classification_report(y_test, y_pred))


print("New Student Prediction:", lr.predict([[6, 84, 9.18, 45]])) 

cf = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cf)

sns.heatmap(cf,annot=True)
plt.show()


print("\nClassification Report:\n", classification_report(y_test, y_pred)) 




# 3 model -- > Naive Bayes 

from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB




data['Participation'] = data['Participation'].map({'No':0, 'Yes':1})
data['Result'] = data['Result'].map({'Fail':0, 'Pass':1})


x = data[['Hours_Study', 'Attendance', 'Test_Score', 'Participation', 'Final_Score', 'Result']]
y = data['Career_Interest']

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
x[['Hours_Study','Attendance','Test_Score','Participation','Final_Score','Result']] = imputer.fit_transform(
    x[['Hours_Study','Attendance','Test_Score','Participation','Final_Score','Result']]
)
x['Participation'] = x['Participation'].fillna(x['Participation'].mode().iloc[0])



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

gb=GaussianNB()
gb.fit(X_train,y_train)
print(gb.score(X_test,y_test)*100)

print(gb.predict([[1,96,90,1,14.11,0]]))