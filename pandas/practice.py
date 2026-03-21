import pandas as pd
data=pd.read_excel(r"C:\Users\SAJLE\Downloads\employee_dataset_2000_rows.xlsx")
print(data)

# 1 --> Dataset ka shape check karo
# print(data.shape)

# 2 --> Column names aur data types dekho
# print(data.columns)

# print(data.dtypes)

# 3 --> Salary column ka mean, min, max nikaalo
# print("mean of salary",round(data['Salary'].mean(),2))

# print(data['Salary'].agg(['min','max','mean']))

#  4 --> Kitni null values hain har column me?
# print(data.isnull().sum())

# Level 2: Null Values Handling

# 1 --> Salary ki null values ko median salary se fill karo
# print(data['Salary'].median())

# data['Salary']=data['Salary'].fillna(76604)
# print(data)

# print(data.isnull().sum())


# 2 --> Age ki null values ko average age se fill karo
# print(round(data['Age'].mean()))

# data['Age']=data['Age'].fillna(36)
# print(data)

# print(data.isnull().sum())

# 3 --> Jinke Experience null hai un rows ko delete karo
# data['Experience']=data.dropna(['Experience'])
data.dropna(subset=['Experience'],inplace=True)
# print(data)

# print(data.isnull().sum())

# print(data.shape)
# data['Experience'].isnull()


# Level 3: Filtering & Conditions

# a --> IT department ke employees nikaalo
# print(data[data['Department']=='IT'])


# b --> Jinki salary > 1 lakh hai unka data
# print((data['Salary']>10000).sum())  #498

# d=data[data['Salary']>=103745]
# print(d)


# c --> Female employees jo Delhi ya Mumbai me hain

# p=data[(data['Gender']=='Female')&((data['City']=="Mumbai")|(data['City']=="Kolkata"))]
# print(p)


# d ->Employees jinki experience 5 se 10 saal ke beech hai
# x=data[data['Experience'].between(5,10)]
# print(x)

# print(x['Experience'].min())

# Level 4: GroupBy & Aggregation
# a --> Department-wise average salary
import pandas as pd
# x=data.groupby("Department")["Experience"].mean()
# print(x)

# b --> City-wise maximum salary
# x=data.groupby("City")["Salary"].max()
# print(x)

# c--> Department-wise employee count
# x=data.groupby("Department")['EmployeeID'].count()
# print(x)

# d --> Gender-wise average experience
# x=data.groupby("Gender")["Experience"].mean()
# print(x)


# 🔹 Level 5: Sorting & Ranking

# a--> Salary ke basis par descending order me sort karo
data=data.sort_values(by="Salary",ascending=False)
print(data)


# b --> Top 10 highest paid employees
# print(data.head(10))


# c --> Department-wise highest salary wala employee
x=data.groupby("Department")["Salary"].idxmax()
res=data.loc[x]
print(res)
