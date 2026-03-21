from collections import Counter
# num=[1,2,3,1,3,1,3,1,2,2,1]
# x=Counter(num)
# print(x)

word="Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data."
x=word.split()
y=Counter(x)
print(y)