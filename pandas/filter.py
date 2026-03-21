import pandas as pd
data=pd.read_csv(r"C:\yash_important data\nba data.csv")
print(data)

# print(data.isnull().sum())

print(data.drop(columns=['Height']))

# 1 filter column 
# filter_colu=data.filter(items=['Name','Team','Salary'])
# print(filter_colu)

# 2 -->  Filtering Columns by Substring
# filter_substring=data.filter(like='a',axis=1)
# print(filter_substring)

# 3 --> Filtering Rows by Index Labels
filter_label=data.filter(items=[0,1,2],axis=0)
print(filter_label)