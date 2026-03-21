# # #  1 count frequency of value
# # #  Hashmap is store data in key value pairs
# # def hashmap(num):
# #     freq={}
# #     for nums in num:
# #         if nums in freq:
# #             freq[nums]+=1
# #         else:
# #             freq[nums]=1
# #     return freq
# # num=[1,1,1,1,2,2,3,3,4,2]
# # print(hashmap(num))


# # 2 --> Check duplicate
# # def check_duplicates(arr):
# #     freq={}
# #     for num in arr:
# #         if num in freq:
# #             freq[num]+=1
# #             return True
# #         else:
# #             freq[num]=1
# #     return False
# # arr = [1,2,3,4]
# # print(check_duplicates(arr))



# # 3 --> Find first non-repeating element
# def first_non(arr):
#     freq={}
#     for num in arr:
#         if num in freq:
#             freq[num]+=1
        
#         else:
#             freq[num]=1

#     for num in arr:
#         if freq[num]==1:
#             return num
        
#     return 0

# arr = [2,3,4,2,3,5]
# print(first_non(arr))


# 4 --> Frequency count 
# def frq(arr):
#     freq={}
#     for num in arr:

#         freq[num]=freq.get(num,0)+1
#     return freq
# arr=[4,4,5,6,6,6]
# print(frq(arr))


# 5 --> Check duplicate
# def check_dup(arr):
#     freq={}
#     for num in arr:
#         freq[num]=freq.get(num,0)+1
#     for num in arr:
#         if freq[num]>1:
#             return True

#     return False

# arr=[1,2,3,4,5,1]
# print(check_dup(arr))


#  6 ---> 

def firstNonRepeating(arr): 
        # Complete the function
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    for num in freq:
        if freq[num]==1:
            return num
            
    return 0
arr=[-1, 2, -1, 3, 2]
print(firstNonRepeating(arr))