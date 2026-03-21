# # implement of tree
# class node: 
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def display(root):
#         if root is None:
#             return None
#         print(root.val,end=" ")
#         node.display(root.left)
#         node.display(root.right)

# root=node(4)
# root.left=node(5)
# root.right=node(8)
# node.display(root)


# Question 1 --> Count total nodes in a binary tree
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def count(root):
#         if root is None:
#             return 0
#         return 1 + node.count(root.left)+node.count(root.right)
# root=node(2)
# root.left=node(4)
# root.right=node(6)

# print(node.count(root))


# Question 2 --> Count leaf nodes in a binary tree.
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def count_leaf(root):
#         if root is None:
#             return 0
#         elif root.left==None and root.right==None:
#             return 1 
        
#         return node.count_leaf(root.left)+node.count_leaf(root.right)
# root=node(2)
# root.left=node(4)
# root.right=node(7)
# print(node.count_leaf(root))


# Question 3 --> Find height of a binary tree
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def count_height(root):
#         count=0
#         if root is None:
#             return 0
#         left_h=node.count_height(root.left)
#         right_h=node.count_height(root.right)
#         return 1+max(left_h,right_h)
# root=node(2)
# root.left=node(4)
# root.right=node(7)
# root.left.left=node(8)
# root.left.right=node(9)
# print(node.count_height(root))


# Question 4 --> Print inorder, preorder, postorder traversal
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
    
#     def inorder(root):
#         if root is None:
#             return
#         node.inorder(root.left)
#         print(root.val,end=" ")
#         node.inorder(root.right)
# root=node(2)
# root.left=node(3)
# root.right=node(4)
# root.left.left=node(6)
# root.left.right=node(8)
# node.inorder(root)


# Question 5 --> Insert an element in Binary Search Tree (BST)
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     # def display(root):
#     #     if root is None:
#     #         return
#     #     print(root.val,end="")
#     #     node.display(root.left)
#     #     node.display(root.right)



#     def insert(self,val):
#         if root is None:
#             return node(val)
#         if val<root.val:
#             if self.left is None:
#                 root.left=node(val)
#             else:
#                 root.left.insert(val)
#         elif val> root.val:
#             if self.right is None:
#                 root.right=node(val)
#             else:
#                 root.right.insert(val)
#         return self
#     def display(root):
#         if root is None:
#             return
#         print(root.val,end=" ")
#         node.display(root.left)
#         node.display(root.right)
# root=node(3)
# root.insert(5)
# root.insert(8)
# print(root.display())





# insert a value in bst 
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def insert_ele(self,val):
        
#         if (val<self.val):
#             if self.left is None:
#                 self.left=node(val)
#             else:
#                 self.left.insert_ele(val)
#         else :
#             if self.right is None:
#                 # root.right is None:
#                 self.right=node(val)
#             else:
#                 self.right.insert_ele(val)
#     def display(root):
#         if root is None:
#             return
#         print(root.val,end=" ")
#         node.display(root.left)
#         node.display(root.right)
# root=node(3)
# root.insert_ele(5)
# root.insert_ele(6)
# print(node.display(root))
            



# Question 6 --> Search an element in BST
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def search_ele(self,target):
        
#         if self.val==target:
#             return "Element found"
#         if target<self.val and self.left is not None:
#             return self.left.search_ele(target)
#         if target>self.val and self.right is not  None:
#             return self.right.search_ele(target)
#         return "Element not found"
        
#     def display(root):
#         if root is None:
#             return
#         print(root.val,end="")
#         root.display(root.left)
#         root.display(root.right)
# root=node(4)
# root.left=node(2)
# root.right=node(7)
# root.right.left=node(5)
# print(root.search_ele(7))



# Question 7 --> Find minimum and maximum value in BST
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def min_max(root):
#         if root is None:
#             return float('inf'),float('-inf')
#         min_left,max_left=node.min_max(root.left)
#         min_right,max_right=node.min_max(root.right)

#         cuur_min=min(root.val,min_left,min_right)
#         cuur_max=max(root.val,max_left,max_right)
#         return (cuur_min,cuur_max)
# root=node(3)
# root.left=node(4)
# root.right=node(10)
# root.left.left=node(5)
# root.left.right=node(9)
# print(node.min_max(root))


# Question 8 --> Check if a tree is a valid BST or not
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def check_bin(self,minimum=float('-inf'),maxmimum=float('inf')):
#         if not(minimum<self.val<maxmimum):
#             return False
#         if self.left:
#             if not self.left.check_bin(minimum,self.val):
#                 return False
#         if self.right:
#             if not self.right.check_bin(self.val,maxmimum):
#                 return False
#         return True


        

# root=node(10)
# root.left=node(5)
# root.right=node(2)
# print(root.check_bin())



# Question 9  --> Find sum of all nodes
class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
    def sum_all(self):
        if self.val is None:
            return 0
        left=0
        right=0
        if self.left:
            
            left=self.left.sum_all()
        if self.right:
            right=self.right.sum_all()
        return (self.val+left+right)
root=node(2)
root.left=node(4)
root.right=node(6)
print(root.sum_all())