import pandas as pd
# df=pd.Series([2,3,1,6])   
# One dimension data ke liye series ka use krte  h 


# df= pd.DataFrame({
#     "name":["yash","xyz","abc"],
#     "age":[20,11,23]
# })
# df=pd.DataFrame(data)

# Data frame 2 dimension ke liye use krete h 



# print(df)



# 1 load data
# data=pd.read_excel(r"C:\yash_important data\ecommerce_sales_data.xlsx")
# print(data.head(1000))
# print(data.info())
# print(data.isnull().sum())
# print(data.fillna(1))

# check stock profit less than 100
# val=data[data["Profit"]<100]
# print(val)

# group by data based on category , sales ,profit
# category=data.groupby('Region')['Quantity'].sum()
# print(category)


# 2 indexing array
# import numpy as np
# arr=np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
# series=pd.Series(arr,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
# print(series[22])


import numpy as np

#  3 loc
# data=pd.Series([20,30,23],index=["ravi","raj","aman"])
# # print(data.loc["ravi"])
# print(data.iloc[0])

# data=pd.read_excel(r"C:\yash_important data\ecommerce_sales_data.xlsx")
# res=pd.Series(data['Region'])
# print(res.iloc[3:10])
# print(res.head(10))



#  4  --> Binary Operations on Pandas Series
# ser1=pd.Series([20,30,19],index=["A","B","C"])
# ser2=pd.Series([10,20,11],index=["A","B","C"])
# # res=ser1+ser2
# res=ser1.add(ser2)
# print(res)


#  5 --> Conversion Operation on Series
# ser=pd.Series([20,12,21,29])
# ser=ser.astype(float)
# res=ser.astype()   # it convert the datatype
# print(ser.dtype) #It check the data type
