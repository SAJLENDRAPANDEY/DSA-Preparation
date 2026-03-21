import pandas as pd
# data={
#     "name":["yash","ravi","raj"],
#     "age":[20,19,22],
#     "marks":[88,60,90]
# }
# print(pd.DataFrame(data))

# 1 column selection
# data = {
#         'Name':['Jai', 'Prince', 'Yash', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification':['Msc', 'MA', 'Mtech', 'Phd']
# }
# df=pd.DataFrame(data)
# # print(df[["Name","Age"]])  #column select

# #  row selection
# # print(df.iloc[0])

# #  loc
# # print(df.loc[df["Name"]=="Yash"])

# daf=


# 3 dataset column 
# data=pd.read_excel(r"C:\yash_important data\ecommerce_sales_data.xlsx",index_col='Product Name')
# res=data['Category']

# print(res)

#  working with missing data
# Checking for Missing Values using isnull() and notnull()


#  check is null
# import numpy as np
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score':[np.nan, 40, 80, 98]}
# data=pd.DataFrame(dict)
# print(data.isnull().sum())

# print(data.fillna(0))

# print(data)

# 5 --> sort value
# arr=pd.Series([2,4,1,8,9,2])
# # print(arr.sort_values(ascending=True))
# print(arr.sort_values(ascending=False))


# 6 -->>rename()
# data=pd.Series([2,4,1,8,9,2])
# arr=data.rename("integer val")
# print(arr)


# 7--> shape()
# data=pd.Series([3,1,3,12,54])
# print(data.shape)

# 8-->ndim
# data=pd.Series([2,3,1,6,8])
# print(data.ndim)

# 9--> copy()
# data=pd.Series([2,3,1,4,5,7,6])
# x=data.copy()
# print(data)
# print(x)

# 10 --> duplicate
# data=pd.Series([2,3,1,4,5,7,6])
# x=data.duplicated()
# print(data)
# print(x)


# 11 --> set index
data=pd.Series([2,4,1,2,3,5])
data.set_index("name")
print(data)