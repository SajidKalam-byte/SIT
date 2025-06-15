# Write a program to print first 5 character of your name using for loop


class nameprint:
    def _init_(self,name):
        self.name=name
        
    def character(self):
        for i in range(0,5):
            print(self.name[i])
            
            
text=input("Enter your name: ")
obj=nameprint()
obj.character(text)