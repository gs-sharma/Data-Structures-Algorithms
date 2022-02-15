class Conversion:

    def __init__(self):
        self.stack = []
        self.result = []
        self.precedence = {
            '(': 0,
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return '$'

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return '$'

    def noGreator(self,e):
        try:
            return self.precedence[self.peek()] >= self.precedence[e]
        except KeyError:
            # this error will arise when stack is empty
            # For given case it will work without this block
            return False


    def infoxToPostfix(self, exp):

        for e in exp:
            if e.isalnum():
                self.result.append(e)
            elif e == '(':
                self.push(e)
            elif e == ")":
                x = self.pop()
                while x != '(':
                    self.result.append(x)
                    x = self.pop()
            else:
                # print(f"len - {len(self.stack) != 0}")
                # print(f"Stack - {self.stack}")
                # print(f"not greator - {e} , {self.noGreator(e)}")
                while (len(self.stack) != 0) and self.noGreator(e):
                    self.result.append(self.pop())
                self.push(e)

        while len(self.stack) != 0:
            self.result.append(self.pop())

        print(f"Given Infix Expression = {exp}")
        print(f"Resultant Postfix Expression = " + "".join(self.result))
        return self.result


exp = "(2*3+4*(5-6))"
convert = Conversion()
convert.infoxToPostfix(exp)
