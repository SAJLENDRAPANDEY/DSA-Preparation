import pandas as pd
import numpy as np

data=pd.read_csv(r"C:\Users\SAJLE\Downloads\employee_dataset.csv")
print(data)


# print(data.isnull().sum())

# print(data.shape)

# print(data)


# print(data.dtypes)


# Level 2 – Missing Values Handling
# a--> Kaunse columns me null values hain
# print(data.isnull().sum())

# b --> Salary ka mean nikaal ke null fill karo
# x=data["Salary"].mean()
# data['Salary']=data["Salary"].fillna(x)
# print(data)

# print(data.isnull().sum())

# c --> Experience ke null rows drop karo
# print(data.dropna(subset=["Experience"],inplace=True))

# print(data.shape)



# Level 3 – Filtering & Sorting
# a--> IT department ke employees nikaalo
# x=data[data['Department']=='IT']
# print(x)


# b --> Salary > 80000 wale employees

# print(data.columns)


# x=data[data['Salary']>8000]
# print(x)

# c--> Top 10 highest salary employees
# print(data.sort_values(by='Salary',ascending=False).head(10))


# Level 4 – New Columns / Feature Engineering
# a--> Experience ke basis par category (Fresher / Mid / Senior)
# print(data['Experience'].min())
# print(data['Experience'].max())
# print(data['Experience'].median())


# data['Experience_category']=pd.cut(data['Experience'],bins=[0,5,15,29],labels=["Fresher", "Mid", "Senior"])
# print(data)

# print(data['Experience'].head(10))


data["Experience_category"]=pd.cut(data['Experience'],bins=[0,5,15,25],labels=("Freseher","Mid","Senior"))
print(data)


# b --> Bonus percentage column add karo
# data["Bonus_percentage"]=data["Bonus"]/data["Salary"]*100
# print(data)


# Level 5 – GroupBy & Aggregation
# a--> Department-wise average salary
# print(data.groupby("Department")["Salary"].mean())


# b --> City-wise employee count
# print(data["City"].count())

# c --> Category-wise average experience
# print(data.columns)

# print(data.groupby("Experience_category")["Experience"].mean())

