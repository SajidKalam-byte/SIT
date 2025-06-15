'''Q1
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
string is valid.'''

class String:
    def __init__(self, l):
        self.l=l
        self.stack= []
        self.precedence = {')': '(', '}': '{', ']': '['}

    def find(self)-> bool:
        for char in self.l:
            if char in self.precedence:
                top_element = self.stack.pop() if self.stack else '#'
                if self.precedence[char]!= top_element:
                    return False
            elif char in self.precedence.values():
                self.stack.append(char)
        return not self.stack


l = ['A', '+', 'B', '*', '(', 'C', '-', 'D', ')', 'E', '/', 'F', '{','}','[]{}']
obj = String(l)
print(obj.find())