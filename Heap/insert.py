# import heapq
# arr=[]
# heapq.heappush(arr,8)
# heapq.heappush(arr,10)

# heapq.heappush(arr,20)

# heapq.heappush(arr,40)

# print(arr)

# pop
# print(heapq.heappop(arr))

# Find kth largest element
# k=2

import heapq
# def smallest_k(nums,k):
#     heap=[]
#     for num in nums:
#         heapq.heappush(heap,num)

#         if len(heap)>k:
#             heapq.heappop(heap)
#     return heap[0]


# nums=[2,1,3,24,42,32]
# k=2
# print(smallest_k(nums,k))

#2 --> Kth Smallest Element 
# def smallest_k(nums,k):
#     heap=[]
#     for num  in nums:
#         heapq.heappush(heap,num)
#     heap.sort()
#     return(heap[k-1])
# nums=[2,1,3,24,42,32]
# k=4
# print(smallest_k(nums,k))



# 3 --> Merge 2 Sorted Arrays Using Heap
# arr1=[1,4,7]
# arr2=[2,10,5,8]
# heap=[]
# merrged=[]
# for x in arr1:
#     heapq.heappush(heap,x)
# for y in arr2:
#     heapq.heappush(heap,y)
# # heap.sort()
# while heap:
#     merrged.append(heapq.heappop(heap))

# print(merrged)


# 4  --> Build Min Heap
# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None

# def min_heap(root,arr):
#     if root is None:
#         return None
#     # arr.sort()
#     root.val=arr.pop(0)
#     min_heap(root.left,arr)
#     min_heap(root.right,arr)
#     return root
# arr=[9, 4, 7, 1, 5]
# arr.sort()

# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)
# root.left.right = Node(50)

# root=min_heap(root,arr)
# print(root.val)




#  5  --> Parent Find Karo
# def parent_node(arr,i):
#     if i==0:
#         return 
#     parent_index=(i-1)//2
#     return parent_index,arr[parent_index]
# arr = [10, 20, 30, 40, 50, 60]
# index,value=parent_node(arr,4)
# print("Parent index :",index)
# print("Parent Value : ",value)


#  6 --> Children Find Karo 
# l=2i+1
# r=2i+2
# def child_node(arr,i):
#     left=2*i+1
#     right=2*i+2
#     return left,arr[left],right,arr[right]
# arr=[5, 10, 15, 20, 25, 30]
# left_i, left_val, right_i, right_val = child_node(arr,1)
# print("Left child is :",left_val)
# print("Right child ",right_val)


# level 2 
#  7 -->  Insert Element in Heap
# def insert_ele(num, val):
#     num.append(val)
#     i=len(num)-1
    
#     while i >0:
#         parent=(i-1)//2
#         if num[parent]>num[i]:
#             num[parent],num[i]=num[i],num[parent]
#             i=parent
#         else:
#             break
# num=[10,20,30,40,50]

# insert_ele(num,5)
# print(num)        



# 8 --> Remove Smallest Element
# def remove_sma(num):
#     if len(num)==0:
#         return 
#     num.sort()
#     return num.pop(0)

# def inorder(root,arr):
#     root.val=arr.pop(0)
#     root.left=inorder(root.left,arr)
#     root.right=inorder(root.right,arr)
#     return root
# inorder(num)
    
# num=[3, 8, 5, 12, 10]




# print(remove_sma(num))
# print(num)






#  9 --> Find 2 Smallest Numbers 
# import heapq
# arr = [7,2,5,1,9]
# k=2
# heapq.heapify(arr)
# first=heapq.heappop(arr)
# second=heapq.heappop(arr)
# print("First smallest :",first)
# print("Second smallest :",second)
# print(arr[:k])


#  10 --> Find Kth Largest Element
# import heapq
# arr=[7,2,5,1,9]
# k=int(input("Enter value: "))
# # heapq.heapify(arr)
# ans=[]
# for num in arr:
#     heapq.heappush(ans,num)
#     if len(ans)>k:
#         heapq.heappop(ans)
# print(ans[0])