class Node:

    def __init__(self, info, nxt=None, prev=None):
        self.info = info
        self.nxt = nxt
        self.prev = prev


class Deque:

    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    # Check isEmpty
    def isEmpty(self):
        return self.size == 0

    # Insert at front
    def insertFront(self, info):
        newNode = Node(info)
        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            newNode.nxt = self.front
            self.front.prev = newNode
            self.front = newNode
        self.size += 1

    # Insert at Rear
    def insertEnd(self, info):
        newNode = Node(info)
        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            newNode.prev = self.rear
            self.rear.nxt = newNode
            self.rear = newNode
        self.size += 1

    # Delete at Front
    def deleteFront(self):
        if self.isEmpty():
            print("Empty Queue")
            return
        else:
            info = self.front.info
            if self.front.nxt is None:
                self.front = self.rear = None
            else:
                self.front = self.front.nxt
                self.front.prev = None
            self.size -= 1
            return info

    # Delete at Rear
    def deleteRear(self):
        if self.isEmpty():
            print("Empty Queue")
            return
        else:
            info = self.rear.info
            if self.rear.prev is not None:
                self.rear = self.rear.prev
                self.rear.nxt = None
            else:
                self.front = self.rear = None
            self.size -= 1
            return info

    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.info)
            temp = temp.nxt
        print('*'*20)



d = Deque()
d.insertFront(10)
d.insertFront(20)
d.display()
d.insertEnd(30)
d.insertEnd(40)
d.display()
d.deleteFront()
d.display()
d.deleteRear()
d.display()
d.deleteRear()
d.display()
d.deleteRear()
d.display()
d.deleteRear()
d.display()