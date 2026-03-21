# import matplotlib.pyplot as plt
# x = [10, 20, 30, 40]
# y = [20, 25, 35, 55]
# fig=plt.figure(figsize=(6,3),facecolor="skyblue")
# ax=fig.add_axes([0.1,0.1,0.5,0.8])
# plt.title("Line chart")
# plt.ylabel("y data")
# plt.xlabel("x label")
# plt.plot(x,y,linestyle="dotted",color="yellow",markersize=5,linewidth=10,marker='o')
# plt.show()


# 2 --> Bar Chart
import matplotlib.pyplot as plt
x=["sun","mon","tue","wed"]
y =[170, 120, 250, 190]
plt.title("Bar charts")
plt.xlabel("Days")
plt.ylabel("value")
plt.bar(x,y,color="green",edgecolor='black',linewidth=4,bbox_inches="tight",pad_inches=0.3,transparent=True)
plt.bar
plt.show()


# histogram
# import matplotlib.pyplot as plt
# x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
#      21, 22, 23, 24, 25, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50]
# plt.hist(x,bins=10,color="green",edgecolor='black',histtype='stepfilled')
# plt.xlabel("frequency")
# plt.ylabel("data")
# plt.title("Histogram")
# plt.show()


# Scatter plot
# import matplotlib.pyplot as plt
# data=[3,2,4,5,6]
# y=["sun","mon","tue","wed","thur"]
# plt.scatter(data,y,linewidths=3,cmap='viridis',marker='D')
# plt.xlabel("data")
# plt.ylabel("days")
# plt.title("Scatter Plot")
# plt.show()


# Pie Chart
# import matplotlib.pyplot as plt
# cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR']
# data = [23, 10, 35, 15, 12]
# explode=[0.1,0.5,0,0,0]
# color=("red","green","blue","black","orange")
# plt.pie(data,labels=cars,explode=explode,colors=color,autopct="%1.2f%%",shadow=True)
# plt.title("Pie chart")
# plt.show()


# box plot
# import matplotlib.pyplot as plt
# data = [ [10, 12, 14, 15, 18, 20, 22],
#          [8, 9, 11, 13, 17, 19, 21],
#          [14, 16, 18, 20, 23, 25, 27] ]
# plt.boxplot(data)
# plt.xlabel("Groups")
# plt.ylabel("Values")
# plt.title("Box plot")
# plt.show()


#  Heatmap
# import matplotlib.pyplot as plt
# import numpy as np
# np.random.seed(0)
# data=np.random.rand(10,10)
# plt.imshow(data)
# plt.show()