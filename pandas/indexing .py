import pandas as pd
data=pd.read_csv(r"C:\yash_important data\nba data.csv")
# print(data)

# print(data.isnull().sum())

# print(data.info())

# print(data.describe())

# first=data["Age"]
# print("/n first row selected ")
# print(first.head())


#1  Indexing with .loc[ ]

#  print single value

# print(data.loc["Avery Bradley"])

# print multiple

# print(data.loc[["Avery Bradley","R.J. Hunter","John Holland"]])

# c -->  Selecting All Rows and Specific Columns
# x=data.loc[:,["Name","Team","Position"]]
# print(x)

# d-->.at[]: Access a single value for a row/column label pair
# print avery bradley age
# val=data.at['Avery Bradley','Age']
# print(val)


# e -->query(): Query the DataFrame using a boolean expression

# result=data.query("Age > 25 and College =='Duke'")
# print(result)


#  f--> # isin
vat=data[data['Name'].isin(['Lance Thomas'])]
print(vat)