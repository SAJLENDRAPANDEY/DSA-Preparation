import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# data={"name":["a","b","c","d","a","c"],"eng":[8,7,5,8,8,5],"hindi":[2,3,4,5,2,6]}
# df=pd.DataFrame(data)
# # print(df)
# # df["duplicated_data"]=df.duplicated()
# # print(df)
# df.drop_duplicates(inplace=True)
# print(df)


#   working with dataset
data=pd.read_csv(r"C:\yash_important data\loan.csv")
print(data.shape)

print(data.duplicated())
print(data.shape)