import pandas as pd
from sklearn.preprocessing import OneHotEncoder
data=pd.read_csv(r"C:\Users\SAJLE\Downloads\loan new data.csv")
print(data.head(5))


data['Gender'].fillna(data['Gender'].mode()[0],inplace=True)

data['education'].fillna(data['education'].mode()[0],inplace=True)
print(data.isnull().sum())
en_data=data[["education","Gender"]]
# print(en_data)

# print(en_data.isnull().sum())
# print(pd.get_dummies(en_data))

ohe=OneHotEncoder()
arr=ohe.fit_transform(en_data).toarray()
x=pd.DataFrame(arr,columns=["education_Bechalor","education_High School or Below","education_Master or Above","education_college","Gender_male"])
print(x)
