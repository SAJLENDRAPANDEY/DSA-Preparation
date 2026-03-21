import pandas as pd
data=pd.read_excel(r"C:\yash_important data\ecommerce_sales_data.xlsx")
# print(data)

# top 10 profit
top_profit=data['Profit']
print(top_profit.head(10))

# top 10 product and profit
top=data[["Product Name","Profit"]]
print(top.head())

# sorting Quantity then top 10
sortimg=data.sort_values(by='Quantity',ascending=True)
print(sortimg.head())

