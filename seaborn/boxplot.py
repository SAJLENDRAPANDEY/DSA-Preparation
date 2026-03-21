import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# data = {'Name': ['ANSH', 'SAHIL', 'JAYAN', 'ANURAG'], 'Age': [21, 23, 20, 24]}
# df=pd.DataFrame(data)
# plt.plot(df.index,df['Age'])
# plt.show()


# 1 --> scatter plot
# data={ 'name':["yash","ravi","raj"],'age':[20,22,19]}
# df=pd.DataFrame(data)
# plt.scatter(x=df.index,y='age',data=df)
# plt.show()


# 2 --> . Box plot
# data={ 'name':['yash','ravi','raj'],'age':[20,44,50]}
# df=pd.DataFrame(data)
# sns.boxplot(y='age',data=df)
# plt.show()

# 3--> Violin Plot
# data={'name':['yash','shreya','raju'],'age':[22,24,24]}
# df=pd.DataFrame(data)
# sns.violinplot(y='age',data=df)
# plt.show()

# 4 --> Bar plot
# data={'name':['yash','ravi','raj'],'age':[23,22,20]}
# df=pd.DataFrame(data)
# sns.barplot(x='name',y='age',data=df,color='green',edgecolor='blue')
# plt.show()

# 5 --> iris dataset
# data=pd.read_csv(r"C:\yash_important data\iris dataset.csv")
# # print(data)
# sns.scatterplot(x='SepalLengthCm',y='SepalWidthCm',data=data,marker='D')
# plt.title("sepalenght vs sepalwidth")
# plt.xlabel("Sepallenghth")
# plt.ylabel("sepalwidth")
# plt.show()


#  6 regression plot
data=pd.read_csv(r"C:\yash_important data\iris dataset.csv")
# print(data)
sns.regplot(x='SepalLengthCm',y='SepalWidthCm',data=data,marker='D')
plt.title("sepalenght vs sepalwidth")
plt.xlabel("Sepallenghth")
plt.ylabel("sepalwidth")
plt.show()