# Count total nodes in a binary tree.
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def count_node(root):
#         if root is None:
#             return 0
#         return 1+node.count_node(root.left)+node.count_node(root.right)
# root=node(2)
# root.left=node(3)
# root.right=node(6)
# print(node.count_node(root))

# Count leaf nodes in a binary tree.

# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def find_leaf(root):
#         if root is None:
#             return 0
#         if root.left==None and root.right==None:
#             return 1
#         return node.find_leaf(root.left)+node.find_leaf(root.right)
# root=node(2)
# root.left=node(3)
# root.right=node(5)
# print(node.find_leaf(root))


# Find height of a binary tree
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def height(root):
#         if root is None:
#             return 0
#         left=node.height(root.left)
#         right=node.height(root.right)
#         return 1+max(left,right)
# root=node(2)
# root.left=node(4)
# root.right=node(6)
# root.left.left=node(8)
# print(node.height(root))


# Insert an element in Binary Search Tree (BST).

# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def insert_ele(self,val):
        
        
#         if val<self.val:
#             if self.left is None:
#                 self.left=node(val)
#             else:
#                 self.left.insert_ele(val)
#         if val>self.val :
#             if self.right is None:
#                 self.right=node(val)
#             else:
#                 self.right.insert_ele(val)
#     def display(root):
#         if root is None:
#             return
#         print(root.val,end=" ")
#         node.display(root.left)
#         node.display(root.right)

# root=node(2)
# root.insert_ele(4)
# root.insert_ele(5)
# print(node.display(root))


# question 1 --> Print all leaf nodes
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def print_leaf(self):
#         if self is None:
#             return
#         if self.left is None and self.right is None:
#             print(self.val,end=" ")
#             return
#         if self.left:
#             self.left.print_leaf()
#         if self.right:
#             self.right.print_leaf()
# root=node(2)
# root.left=node(4)
# root.right=node(6)
# print(node.print_leaf(root))


# Question 2  --> Find sum of only leaf nodes
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def find_sum(self):
#         if self is None:
#             return 0
#         if self.left is None and self.right is None:
#             return self.val
#         left=0
#         right=0
#         if self.left:
#             left=self.left.find_sum()
#         if self.right :
#             right=self.right.find_sum()
#         return left+right
# root=node(2)
# root.left=node(4)
# root.right=node(5)
# print(node.find_sum(root))



# Question 3 --> Find sum of left subtree only
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def sum_left(self):
#         if self is None:
#             return 0
#         if self.left:
#             left=self.left.sum_left()
#         return self.val+left
# root=node(3)
# root.left=node(4)
# root.right=node(5)
# print(root.sum_left())


# Question 4 --> Print all nodes at level 0, 1, 2, 3...

# (Level-order traversal but simple print)

# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def level_tra(root):
#         if root is None:
#             return
#         print(root.val,end=" ")
#         node.level_tra(root.left)
#         node.level_tra(root.right)
# root=node(2)
# root.left=node(3)
# root.right=node(5)
# print(node.level_tra(root))

# Question 5 --> Check if two trees are identical
# class node:
#     def __init__(self,val):
#         self.val=val
#         # self.val2=val2
#         self.left=None
#         self.right=None
#     def check_ide(root1,root2):
#         if root1 is None and root2 is None:
#             return True
#         if root1 is None or root2 is  None:
#             return False
#         return (root1.val==root2.val and
#             node.check_ide(root1.left , root2.left)  and 
#             node.check_ide(root1.right ,root2.right))
# root1=node(2)
# root1.left=node(4)
# root1.right=node(6)


# root2=node(2)
# root2.left=node(4)
# root2.right=node(6)

# print(node.check_ide(root1,root2))



# Question 6 --> Find maximum node value in the tree.

# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def max_val(root):
#         if root is None:
#             return 0
        
#         left=node.max_val(root.left)
#         right=node.max_val(root.right)
#         return max(root.val,left,right)
# root=node(29)
# root.left=node(4)
# root.right=node(6)
# print(node.max_val(root))
        


# Question 7 --> Check if a node is leaf or not.
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def check_leaf(self):
#         # if self is None:
#         #     return False
#         if self.left is None and self.right is None:
#             return True
#         return False
# root=node(2)
# root.left=node(4)
# root.right=node(6)
# print(root.left.check_leaf())


# Question 8 --> Print all nodes that have only one child.
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def print_one(self):
#         res=[]
        
#         if((self.left is None and self.right is not None ) or
#          (self.left is not None and self.right is None)):
#             res.append(self.val)

#         if self.left:
#             res+=self.left.print_one()
#         if self.right:
#             res+=self.right.print_one()
        
#         return res
# root=node(2)
# root.left=node(4)
# root.right=node(5)
# root.left.left=node(8)
# print(root.print_one())
        

# Question 9 --> Print all nodes that have two children.
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def print_node(self):
#         res=[]
#         if (self.left is not None and self.right is not None):
#             res.append(self.val)
#         if self.left:
#             res+=self.left.print_node()
#         if self.right:
#             res+=self.right.print_node()
#         return res
# root=node(2)
# root.left=node(3)
# root.right=node(5)
# root.left.left=node(7)
# root.left.right=node(8)
# print(root.print_node())


# Question 10 --> Find height of only left subtree
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.right=None
#         self.left=None
#     def find_height(self):
#         if self is None:
#             return 0
#         left_h=self.left.find_height() if self.left else 0
#         right_h=self.right.find_height() if self.right else 0

#         return 1 +max(left_h,right_h)
#     def left_sub_h(self):
#         if self.left is None:
#             return 0
#         return self.left.find_height()
    


# root=node(1)
# root.left=node(4)
# root.right=node(6)

# root.left.left=node(3)
# root.left.left.left=node(8)
# print(root.left_sub_h())



# Question 11 --?> Find height of only right subtree.

# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def find_height(self):
        
#         left_h=self.left.find_height() if self.left else 0
#         right_h=self.right.find_height() if self.right else 0

#         return 1+max(left_h,right_h)
#     def right_h(self):
#         if self.right is None:
#             return 0
#         return self.right.find_height()
# root=node(2)
# root.left=node(4)
# root.right=node(6)
# root.left.left=node(8)
# root.right.right=node(9)
# print(root.find_height())


# Question 12 --> Print all nodes in reverse level order.
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def print_reverse(root):
#         if root is None:
#             return []
#         queue=[root]
#         stack =[]
#         while queue:
#             node=queue.pop(0)
#             stack.append(node.val)
#             if node.right:
#                 queue.append(node.right)
#             if node.left:
#                 queue.append(node.left)
#         res=[]
#         while stack:
#             res.append(stack.pop())
#         return res
# root=node(2)
# root.left=node(4)
# root.right=node(5)
# root.left.left=node(6)
# root.left.right=node(8)
# print(node.print_reverse(root))



