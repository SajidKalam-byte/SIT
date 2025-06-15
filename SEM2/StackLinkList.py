class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print("\nInsertion is Success!!!")

    def pop(self):
        if self.top is None:
            print("\nStack is Empty!!!")
        else:
            popped_node = self.top
            self.top = self.top.next
            print(f"\nDeleted element: {popped_node.data}")

    def display(self):
        if self.top is None:
            print("\nStack is Empty!!!")
        else:
            temp = self.top
            print("\nStack elements are:")
            while temp is not None:
                print(f"{temp.data} ---> ", end="")
                temp = temp.next
            print("NULL")

def menu():
    stack = StackLinkedList()
    print("\n:: Stack using Linked List ::")
    while True:
        print("\n****** MENU ******")
        print("1. Push\n2. Pop\n3. Display\n4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            value = int(input("Enter the value to be inserted: "))
            stack.push(value)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("\nWrong selection!!! Please try again!!!")


menu()
