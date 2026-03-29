# # Q 1 -->   max sum subarray 
# def max_sum(arr,k):
#     window_sum=sum(arr[:k])
#     max_sum=window_sum
#     for i in range(k,len(arr)):
#         window_sum+=arr[i]
#         window_sum-=arr[i-k]

#         max_sum=max(max_sum,window_sum)
#     return max_sum
# # arr=[3,2,3,4,1,5]
# print(max_sum([2,1,5,1,3,2],3))



# # Q 2 --> 