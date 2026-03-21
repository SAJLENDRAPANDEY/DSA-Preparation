# # # # create a tree
# # # class node:
# # #     def __init__(self,data):
# # #         self.data=data
# # #         self.left=None
# # #         self.right=None
# # #     def preorder(self,root):
# # #         if root is None:
# # #             return None
# # #         print(root.data,end=" ")
# # #         self.preorder(root.left)
# # #         self.preorder(root.right)
# # #     # def print_node(self,root):
# # #     #     if root is None:
# # #     #         return 0
# # #     #     print(root.data,end=" ")
# # #     #     print(root.left.data)
# # #     #     print(root.right.data)
# # # root=node(2)
# # # root.left=node(4)
# # # root.right=node(8)
# # # root.left.left=node(10)
# # # root.left.right=node(17)
# # # root.preorder(root)


# # # Q1️⃣ Count total nodes in a binary tree
# # # class node:
# # #     def __init__(self,data):
# # #         self.data=data
# # #         self.left=None
# # #         self.right=None
# # #     def count_n(self,root):
# # #         if root is None:
# # #             return 0
# # #         return 1+self.count_n(root.left)+self.count_n(root.right)
# # # root=node(2)
# # # root.left=node(4)
# # # root.right=node(6)
# # # print(root.count_n(root))


# # # Q 3 -->Count leaf nodes in a binary tree
# # class node:
# #     def __init__(self,data):
# #         self.data=data
# #         self.left=None
# #         self.right=None
# #     def count_leaf(self,root):
# #         if root is None:
# #             return 0
# #         # if self.left:
# #         #     while self.left:
# #         elif root.left is None and root.right is None:
# #             return 1
 
# #         return  self.count_leaf(root.left)+self.count_leaf(root.right)
# # root=node(2)
# # root.left=node(3)
# # root.right=node(5)
# # print(root.count_leaf(root))

# # Q 4 --> Find height of binary tree
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def height(self,root):
#         if root is None:
#             return 0
#         # if root.left is None or root.right is None:
#         #     return 1
        
#         left=self.height(root.left)
#         # if self.right:
#         right=self.height(root.right)


#         return 1+max(left,right)
        
# root=node(2)
# root.left=node(4)
# root.right=node(6)
# root.left.left=node(7)
# root.left.right=node(8)
# print(root.height(root))


#  5 -->Print all leaf nodes
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def print_leaf(root):
#     if root is None:
#         return 0
#     if root.left is None and root.right is None:
#         print(root.data,end=" ")
#         return
        
        
#     print_leaf(root.left)
#     print_leaf(root.right)

# root=Node(2)
# root.left=Node(3)
# root.right=Node(5)
# root.left.right=Node(7)
# print(print_leaf(root))

# 


# 6 --> 