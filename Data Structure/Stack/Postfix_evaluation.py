class Evaluation:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return '$'

    def evaluate(self, exp):
        operator = ['+', '-', '*', '/', '^']
        for e in exp:
            if e in operator:
                a = self.pop()
                b = self.pop()
                self.push(str(eval(b + e + a)))
            else:
                self.push(e)

        if len(self.stack) > 1:
            return "Wrong Expression"
        return self.pop()


e = Evaluation()
print(e.evaluate('234*6*+'))
