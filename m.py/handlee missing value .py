import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv(r"C:\yash_important data\loan.csv")
# # print(data.head(10))
# # print(data)

# # print(data.isnull().sum())
# print(data.select_dtypes(include='object').isnull().sum())
# # print(data.select_dtypes(include='object').columns)

# for i in data.select_dtypes(include='object').columns:
#     data[i].fillna(data[i].mode()[0],inplace=True)

# print(data.select_dtypes(include='object').isnull().sum())
 



#        handle missing values using scikit learn

from sklearn.impute import SimpleImputer
si=SimpleImputer(strategy='mean')
# print(data.info())
# print(data.columns)
print(data.select_dtypes(include='float64').columns)
arr=(si.fit_transform(data[['past_due_days']]))
new_dataset=(pd.DataFrame(arr,columns=data.select_dtypes(include='float64').columns))
print(new_dataset)
print(new_dataset.isnull().sum())