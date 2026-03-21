import pandas as pd
data=pd.read_excel(r"C:\Users\SAJLE\Downloads\age_estimatedsalary_purchased_unbalanced.xlsx")
print(data.head(5))

# # print(data["Purchased"].value_counts())


x=data.iloc[:,:-1]
y=data["Purchased"]
# # # print(x)

# # from sklearn.linear_model import LinearRegression
# # from sklearn.model_selection import train_test_split
# # lr=LinearRegression()

# # X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
# # lr.fit(X_train,y_train)
# # # print(lr.predict([[22,20846]]))


# x=data.iloc[:,:-1]
# y=data["Purchased"]

# from imblearn.under_sampling import RandomUnderSampler
# ru=RandomUnderSampler()
# ru_x,ru_y=ru.fit_resample(x,y)
# print(ru_y.value_counts())

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# X_train, X_test, y_train, y_test = train_test_split(ru_x,ru_y,test_size=0.2,random_state=42)
# lr=LogisticRegression()
# lr.fit(X_train,y_train)
# print(lr.score(X_test,y_test*100))

# print(lr.predict([[25,30488]]))







#       Random over sampling
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from imblearn.over_sampling import RandomOverSampler
ro=RandomOverSampler()
ro_x,ro_y=ro.fit_resample(x,y)
print(ro_y.value_counts())
lr=LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(ro_x,ro_y,test_size=0.2,random_state=42)
lr.fit(X_train,y_train)
print(lr.score(X_test,y_test)*100)
