# # Count Values in Pandas Dataframe
# import pandas as pd
# # data=pd.read_excel(r"C:\yash_important data\ecommerce_sales_data.xlsx")

# data = {
#     'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice'],
#     'Age': [25, 30, 25, 35, 30, 25],
#     'City': ['New York', 'Chicago', 'New York', 'San Francisco', 'Chicago', 'New York']
# }
# data=pd.DataFrame(data)
# # print(data)

# # print count unique value
# print(data.count())

# # name count
# print(data['Name'].count())


# # unique value
# # print(data.value_counts().unique())

# # null find
# # print(data.notnull().sum())
# import numpy as np

# # print fill nan data and handle it
# # data.loc[2,"City"]=np.nan
# # print(data)

# # #  handle it
# # print(data['City'].value_counts(dropna=False))

# # print(data.count())


# # group by value count
# x=data.groupby('Age')['Name'].count()
# print(x)