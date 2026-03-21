import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
df=pd.DataFrame({"size":["s","m","xl","xxl","s","m","xxl"]})
# ord_data=[["s","m","xl","xxl"]]
# oe=OrdinalEncoder(categories=ord_data)
# oe.fit(df[["size"]])
# df['size_n']=oe.transform(df[["size"]])
#   oridinal encoding using map function 

ord_data1={"s":0,"m":1,"xl":2,"xxl":3}
df["new_size"]=df["size"].map(ord_data1)

print(df)
# print(x)