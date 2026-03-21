import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data=pd.read_csv(r"C:\Users\SAJLE\Downloads\insurance.csv")
# print(data)

# print(data.info())
# print shape of data
# print(data.shape)

# check is null in data
# print(data.isnull().sum())

# print(data.columns)

# numeric_colums=['age', 'bmi', 'children',  'charges']
# for col in numeric_colums:
#     plt.figure(figsize=(6,4))
#     sns.histplot(data[col],kde=True,bins=20)
# plt.show()


# count plot for check distribution of data
# print(sns.countplot(x=data['sex']))
# plt.show()
# print(sns.countplot(x=data['smoker']))

# plt.show()

# step 2 --> Data cleaning and preprocessing
cleaned_data=data.copy()
# print(cleaned_data)

# print(cleaned_data.isnull().sum())
# print(cleaned_data.shape)
# print(cleaned_data.drop_duplicates(inplace=True))
# print(cleaned_data.shape)

# label encoding
# print(cleaned_data['sex'].value_counts())

cleaned_data['sex']=cleaned_data['sex'].map({"male":0,"female":1})
# print(cleaned_data)

# print(cleaned_data['smoker'].value_counts())
cleaned_data['smoker']=cleaned_data['smoker'].map({"yes":1,"no":0})


cleaned_data.rename(columns={
    'sex':'is_female',

    'smoker':'is_smoker'
},inplace=True)
print(cleaned_data)

cleaned_data=pd.get_dummies(cleaned_data,columns=['region'],drop_first=True)
print(cleaned_data)


# feature engineering and extraction 

cleaned_data['bmi_category']=pd.cut(
    cleaned_data['bmi'],
    bins=[0,18.5,24.9,29.9,float('inf')],
    labels=['underweight','normal','overweight','obese']

)


cleaned_data=pd.get_dummies(cleaned_data,columns=['bmi_category'],drop_first=True)
cleaned_data=cleaned_data.astype('int')

# print(cleaned_data)

# print(cleaned_data.columns)

# sklearn
from sklearn.preprocessing import StandardScaler
cols=['age','bmi','children']
scaler=StandardScaler()
cleaned_data[cols]=scaler.fit_transform(cleaned_data[cols])
print(cleaned_data)

from scipy.stats import pearsonr
