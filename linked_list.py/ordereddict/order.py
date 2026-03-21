from collections import OrderedDict
od=OrderedDict()
od["A"]=1
od["B"]=2
od["C"]=3

od.pop("B")
od["B"]=8

print(od)
