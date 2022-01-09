class Node:
    
    def __init__(self,info,prev = None, nxt=None):
        self.info = info
        self.prev = prev
        self.nxt = nxt
        

class LinkedList:
    
    def __init__ (self):
        self.head = None
        
    def insert_at_begining(self,ele):
        newNode = Node(ele)
        if self.head != None:
            newNode.nxt = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            self.head = newNode
            
    def insert_at_end(self,info):
        newNode = Node(info)
        if self.head != None:
            current = self.head
            while current.nxt != None:
                current = current.nxt
            current.nxt = newNode
            newNode.prev = current
        else:
            self.head = newNode
            
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
ll.insert_at_begining(10)
ll.insert_at_begining(5)
ll.display()
print("*"*10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()
print("*"*10)
ll.delete_node(20)         
ll.display()
print("*"*10)
ll.delete_node(40)         
ll.display()
print("*"*10)
         
