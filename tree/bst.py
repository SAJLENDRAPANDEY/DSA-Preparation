# class node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None

# def search_data(root,key):
#     if root is None or root.data == key:
#         return root

#     if key < root.data:
#         return search_data(root.left, key)
#     else:
#         return search_data(root.right, key)

# root = node(5)
# root.left = node(3)
# root.right = node(8)
# root.left.left = node(2)
# root.left.right = node(4)

# res = search_data(root, 5)

# if res:
#     print("Element found")
# else:
#     print("Element not found")


#  2 --> Insert element in BST
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert_node(root,key):
    if root is None :
        return node(key)
    if key<root.data:
        root.left=insert_node(root.left,key)
    else:
        root.right=insert_node(root.right,key)
    return root
def print_data(root):
    if root is None:
        return 
    print(root.data,end=" ")
    print_data(root.left)
    print_data(root.right)
    
root=node(5)
root.left=node(4)
root.right=node(6)
root=insert_node(root,8)

print("key inserted ")

print(print_data(root))