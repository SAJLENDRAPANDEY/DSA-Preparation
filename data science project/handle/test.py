import pandas as pd

data=pd.read_csv(r"C:\Users\SAJLE\Downloads\Walmart\Walmart 3.csv")

# print(data.isnull().sum())

# print(data.columns)

cat=data.groupby('Category')['Revenue'].sum()
print(cat.sort_values())

# dsa and walmart ka full sql proejct and ml 
