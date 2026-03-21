from collections import namedtuple
student=namedtuple("student",["name","age","marks"])
x=student("yash",20,99)
# print(x.age)
x2=x._replace(age=22)
print(x2)