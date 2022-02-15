class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self,info):
        self.stack.append(info)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1

s = Stack()

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

