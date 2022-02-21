class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.size = 0
        self.front = 0
        self.rear = (self.front + (self.size - 1)) % self.capacity

    def enqueue(self,info):

        if self.size == self.capacity:
            print("Queue is already full, cant add more elements")
            return
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = info
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is Empty")
            return
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1 ) % self.capacity
            self.size -= 1
            return temp

    def display(self):
        temp = self.front
        print('Queue : ')
        for i in range(self.size):
            print(self.queue[temp])
            temp = (temp +1) % self.capacity
        print('*'*20)


q = Queue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
print(f"Dequeue - {q.dequeue()}")
q.display()
q.enqueue(40)
q.display()
q.enqueue(40)
q.display()
