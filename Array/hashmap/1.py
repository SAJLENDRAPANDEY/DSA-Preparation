# # Count frequency of elements
# def count_freq(arr):
#     freq={}
#     for num in arr:
#         freq[num]=freq.get(num,0)+1
#     return freq
# arr=[1,2,1,1,1,2,2,3,3,4,3,2]
# print(count_freq(arr))


# 2 Find duplicate element
def find_duplicate(arr):
    freq={}
    res=[]
    for num in arr:
        freq[num]=freq.get(num,0)+1
    for num in freq:
        if freq[num]>=2:
            res.append(freq[num])
    return res
arr=[1,1,1,2,2,1,2,3,4,4,3,6]
print(find_duplicate(arr))