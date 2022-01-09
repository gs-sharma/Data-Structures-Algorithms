class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    
    def buildBst(self,root,ele):
        if root == None:
            return Node(ele)
        if ele < root.data:
            root.left = self.buildBst(root.left, ele)
        else:
            root.right = self.buildBst(root.right,ele)
        return root
    
    def search(self,root,ele):
        if root is None or root.data == ele:
            return root
        if root.data > ele:
            return slef.search(root.left,ele)
        return self.search(root.right,ele)
        
    def min_value(self,root):
        current = root
        while current.left is not None:
            current = current.left
        return current.data
        
    def max_value(self,root):
        current = root
        while current.right is not None:
            current = current.right
        return current.data
        
    def inOrderTraversal(self,root):
        if root == None:
            return
        self.inOrderTraversal(root.left)
        print(root.data)
        self.inOrderTraversal(root.right)
    
        
root = None
b = BST()
x = [10,5,25,2,7,30]
print(f"Input - {x}")
for ele in x:
    root = b.buildBst(root,ele)
    
b.inOrderTraversal(root)
searched_node = b.search(root,30)
if searched_node == None:
    print("Element Not Found")
else:
    print(f"Found - {searched_node.data}")
    
print(f"Min - {b.min_value(root)}")
print(f"Max - {b.max_value(root)}")  