class Node:
    
    def __init__(self,info,link = None):
        self.info = info
        self.link = link
        

class LinkedList:
    
    def __init__ (self):
        self.head = None
        
    def insert_at_begining(self,info):
        newNode = Node(info)
        if self.head != None:
            newNode.link = self.head
            self.head = newNode
        else:
            self.head = newNode
            
    def insert_at_end(self,info):
        newNode = Node(info)
        if self.head != None:
            current = self.head
            while current.link != None:
                current = current.link
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
        # try using current.info ????
        while current.link !=None:
            if current.link.info == ele:
                temp = current.link
                current.link = temp.link
                temp = None
                return
            current = current.link
        print("Element not Present")
            

    def search_node(self,ele):
        if self.head == None:
            print("List Is Empty")
            return
                
        current = self.head
        #Why not current.link is compared here ????
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
ll.delete_node(20)         
ll.display()
print("*"*10)
ll.delete_node(40)         
ll.display()
print("*"*10)
ll.search_node(5)         
