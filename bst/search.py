#  Q 1 --> Search in BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def print_tree(self,root):
        if root is None:
            return 
        print(root.data,end=" ")
        self.print_tree(root.left)
        self.print_tree(root.right)

    # search
    def search(self,root,key):
        if root is None:
            return False
        if root.data==key:
            return True
        if key<root.data:
           return self.search(root.left,key)
        else:
           return self.search(root.right,key)



    def insert(self,root,key):
        if root is None:
            return Node(key)
        if root.data<key:
           root.left=self.insert(root.left,key)
        else:
            root.right=self.insert(root.right,key)
        return root

    # Delete in BST
    def delete_bst(self,root,key):
        if root is None:
            return root
        # 
        if key<root.data:
            root.left=self.delete_bst(root.left,key)
        if root.data<key:
            root.right=self.delete_bst(root.right,key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # two children
            successor=self.minValue(root.right)
            root.data = successor.data
            root.right = self.delete(root.right, successor.data)
    
    def minValue(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    # is validate
    def isvalid(self,root , low=float('-inf'),high=float('inf')):
        if root is None :
            return True
        if root.data<=low or root.data>=high:
            return False
        
        return (self.isvalid(root.left,low,root.data) and self.isvalid(root.right,root.data,high))
    
    # Kth smallest element
    def kth_smallest(self,root):
        # low=float(-'inf')
        if root is None:
            return 0
        while root.left:
            root=root.left
        return root.data
        
    # Maximum element in BST
    def max_ele(self,root):
        if root is None:
            return 0
        while root.right:
            root=root.right
        return root.data
    
    # Validate BST
    def is_validate(self,root,low=float('-inf'),high=float('inf')):
        if root is None:
            return True
        if root.data<=low or root.data>=high:
            return False
        return (self.is_validate(root.left,low,root.data)and self.is_validate(root.right,root.data,high))
    
    # Delete a node in BST

    def  delete_bst2(self,root,key):
        if root is None:
            return root
        
        if key<root.data:
            root.left=self.delete_bst2(root.left,key)
        if key>root.data:
            root.right=self.delete_bst2(root.right,key)
        else:
            # one children
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # two children
            suc=self.minValue2(root.right)
            root.data=suc.data
            root.right=self.delete(root.right,suc.data)
    def minValue2(self,node):
        current=node
        while current.left:
            current=current.left
        return current
    


    # Kth smallest element in BST
    def kth_smallest(self,root,k):
        res=[]
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            res.append(node.data)
            inorder(node.right)

        inorder(root)
        return res[k-1]

    # optimised
    def kth_small(self,root,k):
        self.ans=None
        self.count=0
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.count+=1
            if self.count==k:
                self.ans=node.data
                return 
            inorder(node.right)

        inorder(root)
        return self.ans


    # Lowest Common Ancestor in BST
    #  lca vo hota h jinke parents means two leaf ke parents
    def lca(self,root,p,q):
        if (p<root.data)and(q<root.data):
            return(self.lca(root.left,p,q))
        if (p>root.data)and(q>root.data):
            return(self.lca(root.right,p,q))
        return root
        

    # Convert sorted array to BST
    
    def convert_bst(self,root):
        arr=[2,3,4,5,6,8]
        def inorder(root,arr):
            left=inorder(root.left,arr)
            root.data=inorder(root.data,arr)
            right=inorder(root.right,arr)

        inorder(root)    
        return root
        
    # Two Sum in BST
    def two_sum(root,k):
        s=set()
        def inorder(node):
            if not node:
                return  False
            if (k-node.data) in s:
                return True
            
            s.add(node.data)
            return (inorder(node.left))or(inorder(node.right))
        
        return inorder(root)
    


    def two_s(root,k):
        
        res=[]
        def bfs(node):
            if node is None:
                return 0
            bfs(node.left)
            res.append(node.data)
            bfs(node.right)

        bfs(root)
    
    
        # res=[]
        low=0
        high=len(res)-1
        while low<=high:
            s=res[low]+res[high]
            if s==k:
                return True
            elif s<k:
                low+=1
            elif s>k:
                high-=1   
        return False

    # Count BST nodes in given range

    def count_n(self,root,l,h):
        if root is None:
            return 0
        if root.data<l:
            return self.count_n(root.left,l,h)
        if root.data>h:
            return self.count_n(root.right,l,h)
        return (1+self.count_n(root.left,l,h)+self.count_n(root.right,l,h))
    
        

root=Node(10)
root.left=Node(6)
root.right=Node(12)
root.left.left=Node(4)
root.left.right=Node(5)

# root.print_tree(root)

        

# print(root.search(root,5))
# print(root.search(root,8))


# insert 20
# root.insert(root,20)
# root.print_tree(root)

# delete 20
# root.delete_bst(root,20)
# root.print_tree(root)


# is valid
# print(root.isvalid(root))

# Kth smallest element
# print(root.kth_smallest(root))

# Maximum element in BST
# print(root.max_ele(root))

# Validate BST
# print(root.is_validate(root))

# Delete a node in BST2
# print(root.delete_bst2(root,5))

# 
# print(root.kth_smallest(root,2))

# print(root.kth_small(root,1))

# Lowest Common Ancestor in BST
# print(root.lca(root,6,12))

# convert array to bst
# print(root.convert_bst(root))


# two sum in bst
# print(root.two_sum( 716))
# print(root.two_s( 16))

# Count BST nodes in given range
# print(root.count_n(root,l=6,h=20))

