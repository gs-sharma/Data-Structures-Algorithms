class Parenthesis:

    def __init__(self):
        self.stack = []

    def check(self,exp):
        for i in range(len(exp)):
            if exp[i] == '{' or exp[i] == '(' or exp[i] == '[' :
                self.stack.append(exp[i])
                continue

            if len(self.stack) == 0 and (exp[i] == '}' or exp[i] == ')' or exp[i] == ']'):
                return False

            if exp[i] == ')':
                ele = self.stack.pop()
                if ele != '(':
                    return False

            if exp[i] == '}':
                ele = self.stack.pop()
                if ele != '{':
                    return False

            if exp[i] == ']':
                ele = self.stack.pop()
                if ele != '[':
                    return False
        if len(self.stack) != 0:
            return False
        else:
            return True

p = Parenthesis()

expr = input("Enter the expression :")
print(p.check(expr))

