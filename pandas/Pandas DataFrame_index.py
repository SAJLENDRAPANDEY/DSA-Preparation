# import pandas as pd
# data=pd.read_csv(r"C:\yash_important data\Employee dataset.csv")
# print(data)

# # set index
# data.set_index("Education",inplace=True)
# print(data)

# # reset index
# df_rest=data.reset_index()
# print(df_rest)

# # 


#  filter data then reset index
import pandas as pd
data = {'ID': [101, 102, 103, 104, 105],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'Dept': ['HR', 'IT', 'IT', 'Finance', 'HR'],
        'Salary': [50000, 60000, 65000, 70000, 55000]}
df=pd.DataFrame(data)
print(df)

# filter based on dept then reset index
# df_it=df[df['Dept']=='IT']
# print(df_it)

# df_it.reset_index(inplace=True,drop=True)
# print(df_it)


# Resetting Index for Multi-Level DataFrames
df.set_index(['ID','Name'],inplace=True,drop=True)
print(df)


df_reset=df.reset_index(level='Name')
print(df_reset)


x=df.sort_values(by=['ID','Salary'],ascending=[True,False])
print(x)