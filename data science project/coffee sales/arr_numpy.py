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

df = df.drop(["Unnamed: 5","Unnamed: 6","Unnamed: 7"], axis=1,errors='ignore')

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

# print(df['revenue'].sum())

# print(df['profit'].sum())

# print(df['country'].nunique())

# level 2
# country wise revenue
# result=(df.groupby('country')['revenue'].sum().reset_index().sort_values(by='revenue',ascending=False))
# result.columns=('Country',"Revenue by country")
# print(result.head(1))


 
# city wise revenue
# result=(df.groupby('city')['revenue'].sum().reset_index())
# result.columns=('City',"sum of revenue by city")
# print(result)


# city wise max revenue
# result=(df.groupby('city')['revenue'].sum().reset_index().sort_values(by='revenue',ascending=False))
# result.columns=('City',"sum of revenue by city")
# print(result.head(1))





# top 5 product revenue
# result=(df.groupby('product_name')['revenue'].sum().reset_index().sort_values(by='revenue',ascending=False))
# result.columns=('Product Name','Revenue')
# print(result.head(5))


# category wise profit
# data=(df.groupby('category')['profit'].sum())

# data.plot(kind='bar')
# plt.show()


# store wise sales performance
# data=(df.groupby('store_id')['revenue'].sum().reset_index().sort_values(by='revenue',ascending=False))
# data.columns=('store_id','max_revenue')
# print(data.head(1))

# data.columns=('store_id','min_revenue')
# print(data.tail(1))


# Level 3

# highest profit product
# data=(df.groupby('product_name')['profit'].sum().reset_index().sort_values(by='profit',ascending=False))
# data.columns=('max_product_name','profit')
# print(data.head(1))

# print(df.groupby('product_name')['profit'].max())

# Kis country me sbse jyada profit h 
# print(df.groupby('country')['profit'].sum().idxmax())

# kis brand ke product jayada sales ho rhe h 
# print(df.groupby('brand')['quantity'].sum().idxmax())

# loss making product
# print(df[df['profit']<0]['product_name'].unique())


# LEVEL 4: Feature Engineering (Advanced)

# profit margin ka column create kro
df['profit_margin']=np.where(df['revenue']!=0,df['profit']/df['revenue']*100,0)
# print(df['profit_margin'])


# Month extract karo
df['month']=pd.to_datetime(df['order_date']).dt.month
# print(df['month'])

# monthly wise revenue
# print(df.groupby('month')['revenue'].sum())

# LEVEL 5: Visualization (Matplotlib)
# top 5 products ka bar chart
# data=df.groupby('product_name')['revenue'].sum().nlargest(5)
# data.plot(kind='bar')
# plt.show()



# Q2 -->monthly sales
# mothly_sales=df.groupby('month')['revenue'].sum()
# mothly_sales.plot(kind='line')
# plt.show()


# Top 10 customers by revenue
# print(df.groupby('customer_id')['revenue'].sum().nlargest(10))



# top product kaun se h aur kyun 
# data=(df.groupby('product_name',as_index=False).agg({'profit':'sum','revenue':'sum'}))
# data['profit_margin']=data['profit']/data['revenue']*100
# data=data.sort_values(by='profit_margin',ascending=False)
# # print(data)
# data.columns = ['Product Name', 'Total Profit', 'Total Revenue', 'Profit Margin']
# print(data.head(5))


# Top products wo hain jinka profit margin highest hai, iska matlab ye products ya to low cost pe produce ho rahe hain ya high pricing power rakhte hain. Ye business ke liye sabse efficient aur profitable segments hain.”


# Kis country me profit high hai?
# print(df.groupby('country')['profit'].sum().idxmax())

# Kya discount se loss ho raha hai?
# sns.scatterplot(x='discount',y='profit',data=df)
# plt.show()


# print(df.groupby('discount').agg({
#     'profit':'mean',
#     'revenue':'mean',
#     'profit_margin':'mean'
# }).reset_index())

# kam discounnt se jayda profit ho rha h 

# q3->Kaunse products loss de rahe hain?
# product_profit=df.groupby('product_name')['profit'].sum()

# loss_product=product_profit[product_profit<0]
# print(loss_product)


# koi bhi product nhi h jo loss de rhe h 

#  q4-->Revenue vs Profit relation
# sns.scatterplot(x='revenue',y='profit',data=df)
# plt.show()


# Q 5 --> Discount vs Profit
# sns.boxenplot(x='discount',y='profit',data=df)
# plt.show()


# Q 6 -->KPI Metrics (Professional Touch)
# total_revenue=df['revenue'].sum()
# print(total_revenue)

# Total Profit
# total_profit=df['profit'].sum()
# print(total_profit)


# Avg Profit
# average_profit=df['profit'].mean()
# print(average_profit)


# Store Performance Ranking
# print(df.groupby('store_id')['profit'].sum().rank(ascending=False))


# Time Series Analysis
df.groupby('month')['profit'].sum().plot()
plt.show()
