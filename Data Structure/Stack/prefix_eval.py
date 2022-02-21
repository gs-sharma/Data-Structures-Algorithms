class Evaluation:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self,val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return '$'

    def evaluate(self,exp):
        operator = ['+', '-', '*', '/', '^']
        for i in range(len(exp)-1, -1, -1):
            if exp[i] in operator:
                a = self.pop()
                b = self.pop()
                self.push(str(eval(b+exp[i]+a)))
            else:
                self.push(exp[i])

        if len(self.stack) > 1:
            return "Wrong Epression"
        return self.pop()

e = Evaluation()
print(e.evaluate('+2**346'))