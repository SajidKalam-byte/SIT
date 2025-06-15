class infix_to_postfix:
    def __init__(self, infix):
        self.infix = infix
        self.postfix = []
        self.stack = []
        
    def precedence(self, op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0
    
    def postfix_con(self):
        for char in self.infix:
            if char.isalnum():
                self.postfix.append(char)
            elif char == '(':
                self.stack.append(char)
            elif char == ')':
                while self.stack and self.stack[-1] != '(':
                    self.postfix.append(self.stack.pop())
                self.stack.pop()
            else:
                while self.stack and self.precedence(self.stack[-1]) >= self.precedence(char):
                    self.postfix.append(self.stack.pop())
                self.stack.append(char)
        
        while self.stack:
            self.postfix.append(self.stack.pop())
    
    def display(self):
        print("Infix Expression: ", ''.join(self.infix))
        print("Postfix Expression: ", ''.join(self.postfix))


l = ['A', '+', 'B', '*', '(', 'C', '-', 'D', ')', 'E', '/', 'F']
obj = infix_to_postfix(l)
obj.postfix_con()
obj.display()
