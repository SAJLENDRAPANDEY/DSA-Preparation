# import pandas as pd
# df=pd.DataFrame({"name":["yash","raj","cow","dog"]})
# print(df)

# from sklearn.preprocessing import LabelEncoder
# lf=LabelEncoder()
# df["en_name"]=lf.fit_transform((df["name"]))
# print(df)

#   using dataset
import pandas as pd
from sklearn.preprocessing  import LabelEncoder
data=pd.read_csv(r"C:\yash_important data\loan.csv")
li=LabelEncoder()
li.fit(data["education"])
data['education']=li.transform(data["education"])
print(data["education"].unique())
print(data.head(3))

