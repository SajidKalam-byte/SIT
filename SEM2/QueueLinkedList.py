class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print("\nInsertion is Success!!!")

    def delete(self):
        if self.front is None:
            print("\nQueue is Empty!!!")
        else:
            temp = self.front
            self.front = self.front.next
            print(f"\nDeleted element: {temp.data}")
            if self.front is None:
                self.rear = None

    def display(self):
        if self.front is None:
            print("\nQueue is Empty!!!")
        else:
            print("\nQueue elements are:")
            temp = self.front
            while temp:
                print(f"{temp.data} ---> ", end="")
                temp = temp.next
            print("NULL")

# Menu-driven program
def menu():
    queue = QueueLinkedList()
    print("\n:: Queue Implementation using Linked List ::")
    while True:
        print("\n****** MENU ******")
        print("1. Insert\n2. Delete\n3. Display\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the value to be inserted: "))
            queue.insert(value)
        elif choice == 2:
            queue.delete()
        elif choice == 3:
            queue.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("\nWrong selection!!! Please try again!!!")


menu()
