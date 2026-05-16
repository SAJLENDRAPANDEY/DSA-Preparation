# Leetcode 1
def two_sum(nums,target):
    res=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return i, j
        i+=1
        j+=1
arr=[2,3,5,6]
target=5
print(two_sum(arr,target))