import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel(r"C:\Users\SAJLE\Downloads\zomato_large_eda_dataset.xlsx")
print(data.head())

# print(data.shape)

# print(data.columns)

# print(data.isnull().sum())
data.drop(columns=['Address'],inplace=True) #because same address is given

data['Cuisine']=data['Cuisine'].bfill()

# handle rating with their mean

# print(data['Rating'].mean) # mean is 2.8 fill using mean
data['Rating']=data['Rating'].fillna(2.8)

# votes ko 0 se fill kr de rhe h because handle outlier to diificult
data['Votes']=data['Votes'].fillna(0)

# handle avg cost for two
# print(data['Average_Cost_for_Two'].median()) #median =1118.5
data['Average_Cost_for_Two']=data['Average_Cost_for_Two'].fillna(1118.5)

# Online_Order 
print(data['Online_Order'].value_counts())
data['Online_Order']=data['Online_Order'].fillna('No')

# Table_Booking
print(data['Table_Booking'].value_counts())
data['Table_Booking']=data['Table_Booking'].fillna('No')
print(data['Table_Booking'].value_counts())

# Phone column ko handle kro 
data['Phone']=data['Phone'].fillna(0)




# print(data.dtypes)
print(data.isnull().sum())

print(data.columns)


# print(data.tail())

# 1 city wise Restaurant count

# print(data.groupby('Restaurant_Name')['City'].count())

# print(data)


#   Bar plot in city count 

# rest_count=data['Restaurant_Name'].value_counts()
# plt.figure(figsize=(8,6))
# plt.bar(rest_count.index, rest_count.values)
# plt.title(" Restaurant count ")
# plt.xlabel("Restaurant Name")
# plt.ylabel("Value count")
# plt.xticks(rotation=45)
# plt.show()


#city wise cuisine count max
print(data.groupby('City')['Cuisine'].value_counts())

# count plot se plot krna h ise
# sns.countplot(x='City',hue='Cuisine',data=data)
# plt.title("city vs cuisine plot")
# plt.xlabel("city")
# plt.ylabel("cuisine")
# plt.legend(loc='upper left')
# plt.show()


# kis restaurant ki rating max h 
# z=data.groupby('Restaurant_Name')['Rating'].max().reset_index()


# sns.barplot(x='Restaurant_Name',y='Rating',data=z)
# plt.title("Max rating restaurant")
# plt.xlabel("restaurant name")
# plt.ylabel("rating")
# plt.xticks(rotation=45)
# plt.show()



# or



# ive_star_data=data[data['Rating']==5.0]

# five_star=five_star_data['Restaurant_Name'].value_counts()#.head(10)


# print(five_star)

# plt.bar(five_star.index,five_star.values,data=data)
# plt.title("Five star rating restaurant")
# plt.xlabel('Restaurant name')
# plt.ylabel('value')
# plt.xticks(rotation=45)
# plt.show()


# which city highest vote
# votes_res=(data.groupby('Restaurant_Name')['Votes'].max().reset_index())

# sns.barplot(x='Restaurant_Name',y='Votes',data=votes_res)
# plt.xticks(rotation=45)
# plt.show()


# city wise sales 
# p=(data.groupby('City')['Average_Cost_for_Two'].max().reset_index())

# sns.lineplot(x='City',y='Average_Cost_for_Two',data=p)

# plt.show()


# check online order or offline
# o=(data['Online_Order'].value_counts().reset_index())
# o.columns=['Online_Order','Count']

# plt.bar(o['Online_Order'],o['Count'])
# plt.title(" online order count")
# plt.xlabel(" order")
# plt.ylabel("count")
# plt.show()


# Rating Distribution
# plt.figure(figsize=(6,4))
# sns.histplot(x=['Rating'],bins=20,kde=True)
# plt.title("Rating Distribution")
# plt.show()



# votes vs rating relationship
# plt.figure(figsize=(3,4))
# sns.scatterplot(x='Votes',y='Rating',data=data)
# plt.title("Votes vs Rating")
# plt.show()


# online order vs rating
# sns.boxplot(x='Rating',y='Online_Order',data=data)
# plt.title("online order vs rating")

# plt.show()


# cost vs ranting
plt.scatter(x='Average_Cost_for_Two',y='Rating',data=data)
plt.title("Cost vs Rating")
plt.show()



print(data)



