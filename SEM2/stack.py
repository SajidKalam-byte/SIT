class Stack:
    def __init__(self, size):
        self.size = size
        self.l = []
        self.top = -1
    

    def push(self,item):
        if self.top == self.size -1:
            print("Stack is full")
        else:
            self.top = self.top +1
            self.l = self.l + [item]
            
    
    def pop(self):
        if self.top == -1:
            print("Stack is empty")
            return
        else:
            item = self.l[self.top]
            self.top = self.top -1
            return item
    def traverse(self):
        print("The items are: ")
        for i in range(0,self.top+1,1):
            print(self.l[i],end=" ")

size = input("Enter the  Stack size: ")
obj = Stack(int(size))
while True:
    print("\n1.Push\n2.Pop\n3.Traverse\n4.Exit\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter the item: ")
        obj.push(item)
    elif choice == "2":
        item = obj.pop()
        print("Popped", item)
    elif choice == "3":
        obj.traverse()
    elif choice == "4":
        break