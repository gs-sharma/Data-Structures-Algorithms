class Node:
    def __init__(self,info,nxt = None):
        self.info = info
        self.nxt = nxt

class StackLinkedList:

    def __init__(self):
        self.head = None

    def push(self,ele):
        newNode = Node(ele)
        newNode.nxt = self.head
        self.head = newNode

    def pop(self):

        if self.head is None:
            return -1
        else:
            info = self.head.info
            self.head = self.head.nxt
            return info

    def peek(self):
        if self.head is None:
            return -1
        else:
            return self.head.info

s = StackLinkedList()
while True:
    print("push")
    print("pop")
    print("peek")
    print("quit")
    do = input("Choose Option :")

    if do == 'push':
        ele = input("Enter the element")
        s.push(ele)
    elif do == 'pop':
        ele = s.pop()
        if ele == -1 :
            print( "Stack is Empty")
        else:
            print(f"Deleted Element - {ele}")
    elif do == 'peek':
        ele = s.peek()
        if ele == -1 :
            print( "Stack is Empty")
        else:
            print(f"Top of stack element - {ele}")
    else:
        break
        break