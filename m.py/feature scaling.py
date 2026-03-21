# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# data=pd.read_csv(r"C:\yash_important data\loan.csv")
# print(data.head(5))
# print(data.isnull().sum())
# data["age"].fillna(data["age"].mean(),inplace=True)
# sns.displot(data["age"])
# plt.show()

# print(data.describe())

# from sklearn.preprocessing import StandardScaler
# ss=StandardScaler()
# ss.fit(data[["age"]])
# data["age"]=pd.DataFrame(ss.transform(data[["age"]]),columns=["x"])
# print(data.head())


# print(data.describe())
# sns.displot(data["age"])
# plt.show()


#         feature scaling using Normalization 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler
data=pd.read_csv(r"C:\Users\SAJLE\Downloads\loan new data.csv")
# print(data.head(5))
# print(data.isnull().sum())
# print(data.describe())

ms=MinMaxScaler()
ms.fit(data[["age"]])
data["age_min"]=ms.transform(data[["age"]])

print(data.head())
plt.figure(figsize=(10,5))