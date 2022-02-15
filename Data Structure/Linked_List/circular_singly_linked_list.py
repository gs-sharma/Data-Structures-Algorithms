class Node:
    def __init__(self, info, nxt=None):
        self.info = info
        self.nxt = nxt


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_begining(self, info):
        newNode = Node(info)
        if self.head is not None:
            current = self.head
            while current.nxt != self.head:
                current = current.nxt
            current.nxt = newNode
            newNode.nxt = self.head
            self.head = newNode
        else:
            self.head = newNode
            self.head.nxt = newNode

    def insert_at_end(self, info):
        newNode = Node(info)
        if self.head is None:
            self.head = newNode
            self.head.nxt = newNode
        else:
            current = self.head
            while current.nxt != self.head:
                current = current.nxt
            current.nxt = newNode
            newNode.nxt = self.head

    def delete_node(self, info):

        # 1 Check if LL is empty
        if self.head is None:
            print("List is Empty")
            return

        # 2 Delete head node
        if self.head.info == info:
            current = self.head
            while current.nxt != self.head:
                current = current.nxt

            self.head = self.head.nxt
            current.nxt = self.head
            return

        # 3 delete in middle
        current = self.head
        while current.nxt != self.head:
            if current.nxt.info == info:
                temp = current.nxt
                current.nxt = temp.nxt
                temp = None
                return
            current = current.nxt

        # 4 Element not found
        print("Element not found")

    def display(self):
        current = self.head
        while current.nxt != self.head:
            print(current.info)
            current = current.nxt
        print(current.info)


ll = CircularLinkedList()
ll.insert_at_begining(10)
ll.insert_at_begining(5)
ll.display()
print("*"*10)

ll.insert_at_end(30)
ll.insert_at_end(40)
ll.display()
print("*"*10)
ll.delete_node(40)
ll.display()
print("*"*10)
ll.delete_node(80)