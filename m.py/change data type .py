import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\SAJLE\Downloads\loan new data3.csv")
print(data.head(5))

print(data.info())

print(data.isnull().sum())

data["terms"] = data["terms"].astype(str).str.strip()


data["terms"].replace("3++","3",inplace=True)

print(data["terms"].value_counts())

data["terms"]=data["terms"].astype("int64")
print(data.info())