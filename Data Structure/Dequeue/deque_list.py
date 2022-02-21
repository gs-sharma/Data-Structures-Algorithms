class Deque:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.size = 0
        self.front = 0
        self.rear = (self.front + (self.size - 1)) % self.capacity

    def insertFront(self, info):

        if self.size == self.capacity:
            print("Queue is already full, cant add more elements")
            return
        else:
            self.front = (self.front - 1 ) % self.capacity
            self.queue[self.front] = info
            self.size += 1

    def insertEnd(self, info):

        if self.size == self.capacity:
            print("Queue is already full, cant add more elements")
            return
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = info
            self.size += 1

    def deleteFront(self):
        if self.size == 0:
            print("Queue is Empty")
            return
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1 ) % self.capacity
            self.size -= 1
            return temp

    def deleteRear(self):
        if self.size == 0:
            print("Queue is Empty")
            return
        else:
            temp = self.queue[self.rear]
            self.rear = (self.rear - 1) % self.capacity
            self.size -= 1
            return temp

    def display(self):
        temp = self.front
        if self.size != 0:
            print('Queue : ')
            for i in range(self.size):
                print(self.queue[temp])
                temp = (temp + 1) % self.capacity
            print('*' * 20)
        else:
            print('Empty Queue')


d = Deque(4)
d.insertFront(10)
d.insertFront(20)
d.display()
d.insertEnd(30)
d.insertEnd(40)
d.insertEnd(50)
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
d.display()
