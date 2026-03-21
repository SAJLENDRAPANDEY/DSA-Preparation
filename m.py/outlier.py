import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv(r"C:\yash_important data\loan.csv")
print(data.head(5))

print(data.info())
print(data.describe())

plt.figure(figsize=(15,4))
sns.boxenplot(x="past_due_days",data=data)

plt.show()



#   outlier remove techinique
q1=data["past_due_days"].quantile(0.25)
# print(q1)

q2=data["past_due_days"].quantile(0.75)
# print(q1)
IQR=q2-q1

min_range=q1-(1.5*IQR)
max_range=q2+(1.5*IQR)
print(min_range,max_range)
print(data.shape)
new_data=data[data["past_due_days"]<=max_range]
print(new_data.shape)