import sys
import time

timer = 0
loading = "Loading: [----------]"
backtrack = '\b' * len(loading)

while timer < 11:
    sys.stdout.write(backtrack + loading)
    sys.stdout.flush()
    loading = loading[:loading.find("-")] + "+" + loading[loading.find("-")+1:]  # Replace first '-' with '='
    time.sleep(1)
    timer += 1

time.sleep(1)
sys.stdout.write(backtrack)



class InfixToPostfix:
    def __init__(self, infix):
        self.infix = infix
        self.postfix = []
        self.stack = [] * 20
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%':2, '^':3}

    def infix_to_postfix(self):
        for char in self.infix:
            if char.isalpha():
                self.postfix.append(char)
            elif char == '(':
                self.stack.append(char)
            elif char == ')':
                while self.stack and self.stack[-1] != '(':
                    self.postfix.append(self.stack.pop())
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
            else:
                while self.stack and self.stack[-1] in self.precedence and self.precedence[self.stack[-1]] >= self.precedence[char]:
                    self.postfix.append(self.stack.pop())
                self.stack.append(char)
        while self.stack:
            self.postfix.append(self.stack.pop())
    def display(self):
        print("Infix :")
        print(" __________________________________________________________________________")
        print("|", self.infix,"      |")
        print("|_________________________________________________________________________|")
        print("\n")
        print("Postfix :")
        print(" __________________________________________________________________________")
        print("|", self.postfix,"                |")
        print("|_________________________________________________________________________|")



l = ['A', '+', 'B', '*', '(', 'C', '-', 'D', ')', '-','E', '/', 'F']

obj = InfixToPostfix(l)
obj.infix_to_postfix()
obj.display()