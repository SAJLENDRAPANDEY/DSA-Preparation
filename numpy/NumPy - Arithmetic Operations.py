import numpy as np

# addition
# x=np.array([2,4,3,7])
# y=np.array([1,3,2,5])
# z=np.add(x,y)
# z1=(x+y)
# print("Addition of two numbers of x and y is :",z)

# print("Addition of two numbers of x and y is :",z1)

#     2 --> Exponentiation (Power)
# a=np.array([4,5,6])
# b=np.array([2])
# c=np.pow(a,b)
# c=a**b
# print(c)



# 3 -- > Modulus Operation
# a=np.array([4,5,8])
# b=np.array([2])
# # c=np.mod(a,b)
# # c=a%b
# print(c)


# 4 --> 

# a=np.array([4,5,8])
# b=np.array([2])



#  numpy broadcasing
# Broadcasting NumPy ka ek smart feature hai jisme different shapes ke --
# arrays ke beech arithmetic operations automatically ho jaate hain — without loop ✨

# 1-->Scalar Broadcasting (Most Common)
# arr=np.array([2,3,1])
# print(arr+3)


# 2 --> Broadcasting in Conditional Operations
# This example checks each age in the array and assigns "Adult" or "Minor" using np.where().

# arr=np.array([18,19,20,22,16])
# res=np.where(arr>18,'adult','minor')
# print(res)

# 3 --> Using Broadcasting for Matrix Multiplication
# m=np.array([[2,4],[1,3]])
# v=np.array([2,4])
# print(m*v)


# 4 --> Centering Data in Machine Learning
# arr=np.array([[10,20],
#               [20,30],
#               [40,30]

# ])
# m=arr.mean(axis=0)
# res=arr-m
# print(res)


# .5 --> 