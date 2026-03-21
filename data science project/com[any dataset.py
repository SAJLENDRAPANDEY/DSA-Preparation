import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel(r"C:\Users\SAJLE\Downloads\realtime_company_dataset_with_nulls.xlsx")
# print(data)



data.fillna(0,inplace=True)

print(data.isnull().sum())


# print(data.columns)

# print max company in county
# print(data['Country'].value_counts())


# #  using bar graph show it 

# data['Country'].value_counts().plot(kind='bar',color='green')
# plt.title("Sum of company country wise")
# plt.xlabel("country")
# plt.ylabel("sum")
# plt.xticks(rotation=45)
# plt.legend('top')
# plt.show()



# 2 Industry wise analysis
# x=data['Industry'].value_counts()

# plt.pie(data['Industry'].value_counts(),labels=x.index,autopct="%1.1f%%")
# plt.show()


#  3 univariate data
# data['Annual_Revenue_Million_USD'].hist(bins=10)
# plt.show()

# 4 bivariate data
#  employee vs profit
# print(data.groupby("Employees")["Profit_Margin_%"].mean())

# sns.barplot(x='Industry',y='Profit_Margin_%',data=data)
# plt.title("Industry vs profit margin")
# plt.show()


# 5 growth vs profit
# plt.scatter(x='Growth_Rate_%',y='Profit_Margin_%',data=data)
# plt.show()


# 6 Outlier detection
# data.boxplot(column='Annual_Revenue_Million_USD')
# plt.show()


# A --> Univariate 
# print(data['Annual_Revenue_Million_USD'].hist(bins=20))
# plt.show()

# data.boxplot(column='Annual_Revenue_Million_USD')

# plt.show()

#  2 --> bar chart -- > country aur industry
# data['Industry'].value_counts().plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()

# data['Country'].value_counts().plot(kind='bar')
# plt.show()

# data['Country'].value_counts().plot(kind='pie',autopct="%1.1f%%")
# plt.show()


# B  ---> Bivariate data
#  1 -->  employee vs revenue
# plt.scatter(x='Employees',y='Annual_Revenue_Million_USD',data=data)
# plt.show()

#  2 -- industry vs avg profit
# print(data.groupby('Industry')['Profit_Margin_%'].mean())

# data.groupby('Industry')['Profit_Margin_%'].mean().plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()

# industry wise growth  rate
# print(data.groupby("Industry")["Growth_Rate_%"].mean())

# data.groupby("Industry")["Growth_Rate_%"].mean().plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()


# C --> Multivariate 
# 1 --> corr heatmap
# sns.heatmap(data.corr(numeric_only=True))
# plt.xticks(rotation=45)
# plt.show()


# D -- missing value
data.isnull().sum().plot(kind='bar')
plt.show()