import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# sales data
import time
start = time.time()
sales = pd.read_excel(r"C:\Data analytics project\reduced_sales_data.xlsx")
# print(f"Loaded in {time.time() - start:.2f} seconds")

# customer data
customer=pd.read_excel(r"C:\Data analytics project\cutomer data.xlsx")

# product data
product=pd.read_excel(r"C:\Data analytics project\product data.xlsx")

# store data
store=pd.read_excel(r"C:\Data analytics project\store data.xlsx")

# calender data
calender=pd.read_excel(r"C:\Data analytics project\calendar.xlsx")

# print(sales.head(5))


# merger all dataset
df=sales.merge(product,on='product_id',how='left')
df=df.merge(customer,on='customer_id',how='left')
df=df.merge(store,on='store_id',how='left')
df=df.merge(calender,left_on='order_date',right_on='date',how='left')

# print(df.isnull())
# print(df.info())
# print(df.shape)

df.drop_duplicates(inplace=True)


# profit flag
df['profit_flag']=np.where(df['profit']>0 , "profit","loss")
# print(df['profit_flag'])

# print(df.shape)


# df.to_excel("final_output.xlsx", index=False)


# print(df.columns)

df = df.drop(["Unnamed: 5","Unnamed: 6","Unnamed: 7"], axis=1)

# print(df.columns)

# ye print krega maximum profit
# print(df['profit'].max())


# isme country ke according sum of revenue kiya h 
# data=(df.groupby('country')['revenue'].sum())

# data.plot(kind='bar')
# plt.show()

# data=(df.groupby('store_type')['revenue'].sum())
# data.plot(kind='bar')
# plt.show()




# print(df.shape)



# pandas basic

print(df['revenue'].sum())

print(df['profit'].sum())

print(df['country'].nunique())