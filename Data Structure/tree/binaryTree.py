class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BT:

    def buildBST(self,root,ele):
        if root is None:
            return Node(ele)
        if ele < root.data:
            root.left = self.buildBST(root.left,ele)
        else:
            root.right = self.buildBST(root.right, ele)
        return root

    def countNodes(self,root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countLeafNode(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return self.countLeafNode(root.left) + self.countLeafNode(root.right)

    def maxdepth(self,root):
        if root is None:
            return 0
        else:
            ld = self.maxdepth(root.left)
            rd = self.maxdepth(root.right)
            return max(ld, rd) + 1

    def iterativeMaxDepth(self, root):
        stack = []
        depth = 0
        if root:
            stack.append((1, root))
        while stack:
            cd, root = stack.pop()
            if root:
                depth = max(cd,depth)
                stack.append((cd+1,root.left))
                stack.append((cd+1,root.right))
        return depth



root = None
b = BT()

for ele in [2,1,33,0,25,40,11,34,7,12,36,13]:
    root = b.buildBST(root,ele)

total = b.countNodes(root)
print(f"Total Nodes = {total}")
leafNodes = b.countLeafNode(root)
print(f"Total number of Leaf Nodes = {leafNodes}")
print(f"max depth = {b.maxdepth(root)}")
print(f"max depth Iterative= {b.iterativeMaxDepth(root)}")