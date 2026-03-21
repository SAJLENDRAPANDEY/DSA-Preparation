# Level 1: Basics (Warm-up)

# 1️⃣ 1D NumPy array banao: [5, 10, 15, 20]
# 2️⃣ 0 se 9 tak ke numbers ka array banao
# 3️⃣ 5 zeros aur 5 ones ka array banao
# 4️⃣ Ek array ka datatype aur shape print karo
# 5️⃣ Python list ko NumPy array me convert karo


# 2 --> 
# import numpy as np
# arr=np.arange(0,10)
# print(arr)
import numpy as np
# 3 --> 
# arr=np.zeros(5)
# arr1=np.ones(5)
# print([[arr],
#       [arr1]])


# 4--> 
# arr=np.array([2,3,1,4,5,2])
# print(arr.shape)
# print(arr.dtype)
# print(arr.ndim)

# 5 -->
# list=[1,2,3,1,3,5]
# arr=np.array(list)
# print(type(arr))
# print(type(list))




# 8-->Array ka square nikalo
# arr=np.array([2,4,6,8])
# x=arr**2
# print(x)

# 9️⃣ Array ka sum aur mean find karo

# 13️⃣ 3*2 ka matrix banao
# arr=np.array([[2,3],
#               [5,6],
#               [8,3]])
# print(arr)



# 14️⃣ Matrix ka shape print karo
# print(arr.shape)
# print(arr.ndim)
# 15️⃣ First row aur second column print karo
# print(arr[0][1])
# 16️⃣ Matrix ke sab elements ko 2 se multiplay karo
# x=arr*2
# print(x)



# 20️⃣ Array [5,12,17,20,25] me se sirf even numbers print karo
# def even(arr):
#     res=[]
#     for i in range(len(arr)):
#         if arr[i]%2==0:
#             res.append(arr[i])
#             i+=1
#     return res
# arr=[5,12,17,20,25]
# print (even(arr))


# or 


# arr=np.array([5,12,17,20,25])
# even_num=arr[arr%2==0]
# print(even_num)

# 21️⃣ Array me se max aur min element nikalo
# arr=np.array([5,12,17,20,25])
# print(max(arr))
# print(min(arr))

# 22️⃣ Array ke elements jo 10 se bade ho unko print karo
# arr=np.array([5,12,17,20,25])

# res=arr[arr>10]
# print(res)


# 23️⃣ 5 random numbers (0–1) ka array banao

# arr=np.random.rand(5)
# print(arr)
# 24️⃣ 1 se 100 ke beech ke 10 random integers generate karo
# arr=np.random.randint(1,100,10)
# print(arr)
# 25️⃣ Array ko ascending order me sort karo 