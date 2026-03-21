# # # import pandas as pd
# # # import seaborn as sns
# # # import matplotlib.pyplot as plt
# # # dataset=pd.read_excel(r"C:\Users\SAJLE\Downloads\age_salary_purchased_dataset.xlsx")
# # # dataset.drop(columns=['EstimatedSalary'],inplace=True)
# # # # print(dataset.head(5))
# # # # sns.scatterplot(x='Age',y='Purchased',data=dataset)
# # # # plt.show()
# # # x=dataset[['Age']]
# # # y=dataset['Purchased']
# # # from sklearn.model_selection import train_test_split
# # # from sklearn.linear_model import LogisticRegression
# # # lr=LogisticRegression()
# # # X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=0.2,random_state=80)
# # # lr.fit(X_train,y_train)
# # # # print(lr.score(X_test,y_test)*100)
# # # print(lr.predict([[20]]))

# # # sns.scatterplot(x='Age',y='Purchased',data=dataset)
# # # sns.lineplot(x='Age',y=lr.predict(x),data=dataset,c='red')
# # # plt.show()
 



# # #        logistic regression with multiple input
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # dataset=pd.read_excel(r"C:\Users\SAJLE\Downloads\logistic_regression_dataset_balanced.xlsx")
# # # print(dataset.head(5))
# # # sns.scatterplot(x="CGPA",y="Score",data=dataset,hue="Placed")
# # # plt.show()

# # x=dataset.iloc[:,:-1]
# # y=dataset["Placed"]
# # # print(x)

# # from sklearn.model_selection import train_test_split
# # X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=0.2,random_state=33)
# # from sklearn.linear_model import LogisticRegression
# # lr=LogisticRegression()
# # lr.fit(X_train,y_train)
# # # print(lr.score(X_test,y_test)*100)
# # print(lr.predict([[7.47,458]]))



# #   polynomial features  

# import pandas as pd
# import seaborn  as sns
# import matplotlib.pyplot as plt
# from mlxtend.plotting import plot_decision_regions
# data=pd.read_excel(r"C:\Users\SAJLE\Downloads\polynomial_dataset.xlsx")
# print(data.head(5))

# # sns.scatterplot(x="data1",y="data2",data=data,hue="output")
# # plt.show()

# x=data.iloc[:,:-1]
# y=data["output"]
# # print(x)

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# lr=LogisticRegression()
# X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=0.2,random_state=36)
# lr.fit(X_train,y_train)
# print(lr.score(X_test,y_test)*100)

# plot_decision_regions(x.to_numpy(),y.to_numpy(),clf=lr)
# plt.show()



#  logistic regression using multiclasss classification

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\yash_important data\iris new.csv")
print(data.head(5))
print(data["species"].unique())

x=data.iloc[:,:-1]
y=data["species"]

# print(x)


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42,)
lr=LogisticRegression(multi_class="ovr")
lr.fit(X_train,y_train)
# print(lr.score(X_test,y_test)*100)


lr1=LogisticRegression(multi_class="multinomial")
lr1.fit(X_train,y_train)
print(lr1.score(X_test,y_test)*100)