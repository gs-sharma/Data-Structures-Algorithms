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
    
    def search(self, root, ele):
        if root is None or root.data == ele:
            return root
        if root.data > ele:
            return self.search(root.left, ele)
        return self.search(root.right, ele)
        
    def min_value(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.data
        
    def max_value(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current.data
        
    def inOrderTraversal(self, root):
        #left-root-right
        if root == None:
            return
        self.inOrderTraversal(root.left)
        print(root.data)
        self.inOrderTraversal(root.right)

    def iterativeInOrder(self,root):
        current = root
        stack = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data)
                current = current.right
            else:
                break

    def preOrder(self, root):
        #root-left-right
        if root is None:
            return
        else:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def iterativePreOrder(self, root):
        if root is None:
            return
        stack = []
        stack.append(root)

        while stack:
            current = stack.pop()
            print(current.data)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def postOrder(self, root):
        #left-right-root
        if root is None:
            return
        else:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)

    def iterativePostOrder(self, root):
        #left-right-root

        if root is None:
            return
        stack = []
        result = []
        stack.append(root)
        while stack:
            current = stack.pop()
            result.append(current.data)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        while result:
            current = result.pop()
            print(current)

    def iterativePostOrder2(self,root):
        if root is None:
            return
        stack = []
        prev = None
        stack.append(root)
        while stack:
            current = stack[-1]
            if prev is None or prev.left == current or prev.right ==current:
                if current.left:
                    stack.append(current.left)
                elif current.right:
                    stack.append(current.right)
                else:
                    print(current.data)
                    stack.pop()
            elif prev == current.left:
                if current.right:
                    stack.append(current.right)
            else:
                print(current.data)
                stack.pop()

            prev = current

    def successor(self,root):
        root = root.right
        while root.left:
            root = root.left
        return root.data

    def predecessor(self,root):
        root = root.left
        while root.right:
            root = root.right
        return root.data

    def deletion(self,root,key):
        if root is None:
            return None

        if key < root.data:
            root.left = self.deletion(root.left, key)
        elif key > root.right:
            root.right = self.deletion(root.right,key)
        else:
            if not (root.right or root.left):
                root = None
            elif root.right:
                root.data = self.successor(root)
                root.right = self.deletion(root.right, root.data)
            else:
                root.data = self.predecessor(root)
                root.left = self.deletion(root.left, root.data)

            return root



        
root = None
b = BST()
x = [16, 8, 24, 6, 12, 18, 28, 4, 6, 14, 26, 30]
print(f"Input - {x}")
for ele in x:
    root = b.buildBst(root, ele)

print('In-Order traversal')
b.inOrderTraversal(root)
print('Iterative In-Order traversal')
b.iterativeInOrder(root)
searched_node = b.search(root, 30)
if searched_node is None:
    print("Element Not Found")
else:
    print(f"Found - {searched_node.data}")
    
print(f"Min - {b.min_value(root)}")
print(f"Max - {b.max_value(root)}")

print("Pre-Order Traversal")
b.preOrder(root)
print("Pre-Order Iterative Traversal")
b.iterativePreOrder(root)
print("Post-Order Traversal")
b.postOrder(root)
print("Iterative Post-Order Traversal")
b.iterativePostOrder(root)
print("Iterative Post-Order Traversal - using single stack")
b.iterativePostOrder2(root)