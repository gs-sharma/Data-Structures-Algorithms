class Node:
    
    def __init__(self,info,prev = None, nxt=None):
        self.info = info
        self.prev = prev
        self.nxt = nxt
        

class LinkedList:
    
    def __init__ (self):
        self.head = None
        self.tail = None
        
    def insert_at_begining(self,ele):
        newNode = Node(ele)
        if self.head != None:
            newNode.nxt = self.head
            self.head.prev = newNode
            self.head = newNode

        else:
            self.head = newNode
            self.tail = newNode

    def insert_at_end(self,info):
        newNode = Node(info)
        if self.head != None:
            current = self.head
            while current.nxt != None:
                current = current.nxt
            current.nxt = newNode
            newNode.prev = current
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def insert_at_end_tail(self,info):
        newNode = Node(info);
        if self.tail is not None:
            self.tail.nxt = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def insert_at_pos(self,info,pos):
        newNode = Node(info)
        count = 1;
        current = self.head
        while current.nxt is not None and count != pos-1:
            current = current.nxt
            count += 1
        newNode.nxt = current.nxt
        newNode.nxt.prev = newNode
        newNode.prev = current
        current.nxt = newNode

    def delete_node(self,ele):
        if self.head == None:
            print("List Is Empty")
            return
                
        if self.head.nxt == None:
            if self.head.info == ele:
                temp = self.head
                self.head = None
                temp = None
                return
            else:
                print("Element Not Found")
                return
        
        #delete node in middle
        #Last element not covered - Why
        temp = self.head.nxt
        while temp.nxt != None:
            if temp.info == ele:
                temp.prev.nxt = temp.nxt
                temp.nxt.prev = temp.prev
                temp = None
                return
            temp = temp.nxt
        
        #Check last element
        if temp.nxt == ele:
            temp.prev.nxt = temp.nxt
            temp = None
            return
        print("Element is not Found in List")

    def display(self):
        if self.head == None:
            print("List Is Empty")
            return
        current = self.head
        while current != None:
            print(current.info)
            current = current.nxt
            

ll = LinkedList()
print('Add 10 and then 5 at begining')
ll.insert_at_begining(10)
ll.insert_at_begining(5)
ll.display()
print("*"*10)
print('Add 20 and then 30 at end')
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()
print("*"*10)
print('Add 200 and then 300 at end')
ll.insert_at_end_tail(200)
ll.insert_at_end_tail(300)
ll.display()
print("*"*10)
print('Add 8 at index 2  and then 9 at index 3 ')
ll.insert_at_pos(8, 2)
ll.insert_at_pos(9,3)
ll.display()
print("*"*10)
print('Delete 20')
ll.delete_node(20)         
ll.display()
print("*"*10)
print('Delete 40')
ll.delete_node(40)         
ll.display()
print("*"*10)
         
