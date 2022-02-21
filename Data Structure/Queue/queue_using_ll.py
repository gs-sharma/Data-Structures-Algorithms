class Node:
    def __init__(self, info, nxt=None):
        self.info = info
        self.nxt = nxt

class Queue:

    def __init__(self):
        self.front = self.rare = None

    def enqueue(self, info):
        newNode = Node(info)
        if self.rare is not None:
            self.rare.nxt = newNode
            self.rare = newNode
        else:
            self.rare = self.front = newNode

    def dequeue(self):
        if self.front is not None:
            info = self.front.info
            self.front = self.front.nxt
            if self.front is None:
                self.rare = None
            return info
        else:
            print("Queue is Empty")
            return

    def display(self):
        temp = self.front
        print('Queue :')
        while temp is not None:
            print(temp.info)
            temp = temp.nxt
        else:
            print('*'*20)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(f"Dequeue - {q.dequeue()}")
q.display()
