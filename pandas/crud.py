# # # # # 1 --> Create: Creating Dataframe
# # # import pandas as pd
# # # # data={
# # # #     "Name":["Yash","om","ajay"],
# # # #     "Age":[22,32,21],
# # # #     "Marks":[88,74,66]
# # # # }
# # # # data=pd.DataFrame(data)
# # # # print(data)


# # # # 2 --> Creating a DataFrame from Lists
# # # name=["yash","raj","abhi"]
# # # age=[22,32,42]
# # # marks=[90,67,88]
# # # data={
# # #     "names":name,
# # #     "ages":age,
# # #     "mark":marks

# # # }
# # # res=pd.DataFrame(data)
# # # print(res)

# # # 3 --> Read: Reading Dataframe

# # import pandas as pd
# # # data=pd.read_excel(r"C:\yash_important data\ecommerce_sales_data.xlsx")
# # data = {
# #         "Name": ["Eve", "Jack", "Charlie", "Henry", "John"],
# #         "Age": [25, 30, 35, 40, 45],
# #         "City": ["NY", "LA", "SF", "Houston", "Seattle"]
# # }
# # data=pd.DataFrame(data)
# # # print(data.head(2))
# # # print(data.tail(2))

# # # print only column name 
# # # print(data.columns)

# # # print data type
# # # print(data.dtypes)

# # # descriptive statics
# # # print(data.describe())

# # # accessing column
# # # print(data[["Name","Age"]])


# # # Finding Unique Values in a Column
# # # print(data["Name"].unique())

# # # Slicing Rows
# # # print(data.iloc[1:3])

# # # Label-Based Indexing
# # data.set_index("Name",inplace=True)

# # # using name accessing element



# #  5 --> Update: Modifying Data in Pandas
# # import pandas as pd
# # data={'Name': ['Eve', 'Jack', 'Charlie', 'Henry', 'John'],
# #         'Age': [25, 30, 35, 40, 45],
# #         'City': ['NY', 'LA', 'SF', 'Houston', 'Seattle']}
# # df=pd.DataFrame(data)
# # print(df)

# # a --> Updating a Single Value (change jack is 50)
# # df.loc[df['Name']=='Jack','Age']=50
# # print(df)

# # b --> Updating an Entire Column
# # df['City']=['Delhi','Gurgaon','mumbai','noida','ncr']
# # print(df)

# # 6 -->  Delete: Removing Data in Pandas

# import pandas as pd
# data={'Name': ['Eve', 'Jack', 'Charlie', 'Henry', 'John'],
#         'Age': [25, 30, 35, 40, 45],
#         'City': ['NY', 'LA', 'SF', 'Houston', 'Seattle']}
# df=pd.DataFrame(data)
# # print(df)

# # a --> Delete a Column (delete city)
# # df=df.drop('City',axis=1)
# # print(df)

# # b --> Delete a Row
# # df=df.drop(2,axis=0)
# # print(df)


# # c -->  Delete Rows Based on Condition
# # df=df[df['Age']!=30]
# # print(df)

# # d --> Delete entire dataset
# df=pd.DataFrame(df)
# del df
# # print(df)