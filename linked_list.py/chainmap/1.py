from collections import ChainMap
x1={"a":1,"b":2}
x2={"c":3,"d":4}
x=ChainMap(x1,x2)
print(x)

print(x["b"])

# Adding / Updating Values
x1["a"]=6
print(x1)

# 