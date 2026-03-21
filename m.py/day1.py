import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\yash_important data\loan.csv")
print(data.head(5))

# print(data.shape)

print(data.isnull().sum().sum())

missing_values=(data.isnull().sum().sum()/(data.shape[0]*data.shape[1]))*100
print("Missisng value",missing_values)

each_column=(data.isnull().sum()/data.shape[0])*100
print("Each column missing values",each_column)
sns.heatmap(data.isnull())
plt.show()

