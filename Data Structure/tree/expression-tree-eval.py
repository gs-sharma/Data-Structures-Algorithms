class Node:

    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class ExpressionTree:

    def evaluate(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data

        left = self.evaluate(root.left)
        right = self.evaluate(root.right)

        return str(eval(left + root.data + right))


root = Node('*')
root.left = Node('+')
root.right = Node('*')
root.left.left = Node('2')
root.left.right = Node('3')
root.right.left = Node('4')
root.right.right = Node('+')
root.right.right.left = Node('5')
root.right.right.right = Node('6')

e = ExpressionTree()
print(e.evaluate(root))