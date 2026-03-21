import pandas as pd
data=pd.read_excel(r"C:\Users\SAJLE\Downloads\employee_hr_dataset_2000_rows.xlsx")
print(data)



# print(data["Salary"].median())
# meadian se salary fill ho gyi h 
data['Salary']=data["Salary"].fillna(105026.5)

# b--> IT department ke high salary employees kaun hain?
# print(data['Salary'].max())#179912.0
# print(data['Salary'].min())#25028.0
# print(data['Salary'].median())#105026.5

# x=data[data['Department']=='IT']['Salary'].max()
# print(x)

# print(data.groupby("Department")['Salary'].max())


# c--> Kaunse department me zyada log company chhod rahe hain?
# print(data["Attrition"])

# x=data[data["Attrition"]=='Yes'].groupby('Department').size()
# print(x)

# print(data.isnull().sum())

# d--> Fresher / Mid / Senior distribution
# print(data['Experience'].agg(["median","min","max"]))

# bins=[0,2,17,34]
# label=["Fresher","Mid","Senior"]
# data["Category_experience"]=pd.cut(data['Experience'],bins=bins,labels=label)
# print(data)

# e --> Har saal kitne employees join hue?
# data["Joining year"]=data['Joining_Date'].dt.year
# print(data[data["Joining year"]>2020].groupby("Department").size())


# f--> 