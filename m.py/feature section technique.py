import pandas as pd
from mlxtend.feature_selection import SequentialFeatureSelector
data=pd.read_csv(r"C:\yash_important data\diabetes.csv")
# print(data.head(5))
x=data.iloc[:,:-1]
y=data["Outcome"]
# print(x)
# print(x.shape)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
fs=SequentialFeatureSelector(lr,k_features=5,forward=True)
fs.fit(x,y)
print(fs.feature_names)

print(fs.k_feature_names_)

print(fs.k_score_)
