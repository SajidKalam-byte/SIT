'''Q4
Given two strings s and t, return true if they are equal when both are typed into empty text
editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".'''

class String:
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def editors(self)-> bool:
        while True:
            for char in self.s[0:len(self.s):1]:
                if char == '#':
                    self.s = self.s[:-1]
            print("This is S:", self.s)
            for char in self.t[0:len(self.t):1]:
                if char == '#':
                    self.t = self.t[:-1]
            print("This is T:", self.t)
            if self.s == self.t:
                return True
            else:
                return False
            
obj = String("ab#c","ad#c")
print(obj.editors())
        