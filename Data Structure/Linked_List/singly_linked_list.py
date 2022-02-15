class Node:
    
    def __init__(self,info,link = None):
        self.info = info
        self.link = link
        

class LinkedList:
    
    def __init__ (self):
        self.head = None
        self.tail = None
        
    def insert_at_begining(self,info):
        newNode : Node = Node(info)
        if self.head != None:
            newNode.link = self.head
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
            
    def insert_at_end(self,info):
        newNode = Node(info)
        if self.head != None:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def insert_at_end_tail(self,info):
        newNode = Node(info)
        if self.tail is not None:
            self.tail.link = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def insert_at_pos(self,info,pos):
        newNode = Node(info)
        count = 1
        if self.head != None:
            current = self.head
            while current.link is not None and count != pos-1:
                current = current.link
                count += 1
            newNode.link = current.link
            current.link = newNode
        else:
            self.head = newNode
            
    def delete_node(self,ele):
        if self.head == None:
            print("List Is Empty")
            return
                
        if self.head.info == ele:
            temp = self.head
            self.head = temp.link
            temp = None
            return
        
        current = self.head

        while current.link !=None:
            if current.link.info == ele:
                temp = current.link
                current.link = temp.link
                if temp.link is None:
                    self.tail = current
                    print(f"tail - {current.info}")
                temp = None
                return
            current = current.link
        print(f"Element - '{ele}' not Present")
            

    def search_node(self,ele):
        if self.head == None:
            print("List Is Empty")
            return
                
        current = self.head

        while current != None:
            if current.info == ele:
                print("Element Found :")
                print(current.info)
            current = current.link  
            
       
    def display(self):
        current = self.head
        while current != None:
            print(current.info)
            current = current.link
            

ll = LinkedList()
ll.insert_at_begining(10)
ll.insert_at_begining(5)
ll.display()
print("*"*10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()
print("*"*10)
ll.insert_at_end_tail(200)
ll.insert_at_end_tail(300)
ll.display()
print("*"*10)
ll.insert_at_pos(8, 2)
ll.insert_at_pos(9,3)
ll.display()
print("*"*10)
ll.delete_node(20)         
ll.display()
print("*"*10)
ll.delete_node(40)         
ll.display()
print("*"*10)
ll.search_node(5)         
print("*"*10)
ll.delete_node(300)
ll.display()