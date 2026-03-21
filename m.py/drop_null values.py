import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data_set=pd.read_csv(r"C:\yash_important data\loan.csv")
print(data_set.head(5))
print(data_set.shape)


data_set.drop(columns=(["past_due_days","paid_off_time"]),inplace=True)
print(data_set.isnull().sum())
print(data_set.dropna(inplace=True))
print(data_set.shape)
sns.heatmap(data_set.isnull())
plt.show()