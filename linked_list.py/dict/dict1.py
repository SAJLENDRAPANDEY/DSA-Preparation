dict1={
    "name":"yash",
    "age":20,
    "marks":89
}

# # access element using key 
# # print(dict1["name"])

# # q 2 --> add element in dict
# # dict1["city"]="delhi"

# #  Q3 --> delete element in dict

# # dict1.pop("name")

# # Q4 --> delete key 
# # del dict1["age"]

# # Q5 --> Check if key exists 

# # if "name" in dict1:
# #     print("Key exist in dictionary")
# # else:
# #     print("not exist")


# # Q 6 --> Print all values
# # print(dict1.keys())

# # print(dict1.values())

# # Q 7 --> print key and values 

# for key,val in dict1.items():
#     print(key,val)
# print(dict1)



#  logic based question

#  Q 1--> Count frequency of elements
# list=[1,3,1,2,1,2,3,1,1]
# freq={}
# for i in list:
#     freq[i]=freq.get(i,0)+1

# print(freq)

# Q 2 --> Create dictionary from keys and values.

# key=["name","age"]
# value=["yash",20]
# res=dict(zip(key,value))
# print(res)

# Q 3 --> Get value of "marks" without error.
# print(dict1.get("sub","Not found"))

# Q 4 --> Frozen set
# s=set(["male","female","boy"])
# s.add("men")
# print(s)
# print(type(s))

# s=frozenset(["male","female","boy"])
# # s.add("men")
# print(s)
# print(type(s))


# Q 5 --> Adding elements to Sets
s=set(["male","female","boy"])
# s.add("girl")
# print(s)

# q6 --> find union Union of Sets
s1=set(["male","boy","girl"])
# x=s.union(s1)
# print(x)

