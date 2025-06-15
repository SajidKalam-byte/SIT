class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            self.head.prev = last.next = new_node
            self.head = new_node
        print("Insertion success!!!")

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            last = self.head.prev
            new_node.prev = last
            new_node.next = self.head
            last.next = self.head.prev = new_node
        print("Insertion success!!!")

    def insert_after(self, value, location):
        if self.head is None:
            print("List is empty! Inserting as the first node.")
            self.insert_at_beginning(value)
            return
        temp = self.head
        while True:
            if temp.data == location:
                new_node = Node(value)
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node
                print("Insertion success!!!")
                return
            temp = temp.next
            if temp == self.head:
                break
        print("Given node is not found in the list!!!")

    def delete_beginning(self):
        if self.head is None:
            print("List is Empty!!! Deletion not possible!!!")
        elif self.head.next == self.head:
            self.head = None
            print("Deletion success!!!")
        else:
            last = self.head.prev
            self.head = self.head.next
            self.head.prev = last
            last.next = self.head
            print("Deletion success!!!")

    def delete_end(self):
        if self.head is None:
            print("List is Empty!!! Deletion not possible!!!")
        elif self.head.next == self.head:
            self.head = None
            print("Deletion success!!!")
        else:
            last = self.head.prev
            last.prev.next = self.head
            self.head.prev = last.prev
            print("Deletion success!!!")

    def delete_specific(self, value):
        if self.head is None:
            print("List is Empty!!! Deletion not possible!!!")
            return
        temp = self.head
        while True:
            if temp.data == value:
                if temp == self.head:
                    self.delete_beginning()
                    return
                elif temp.next == self.head:
                    self.delete_end()
                    return
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    print("Deletion success!!!")
                    return
            temp = temp.next
            if temp == self.head:
                break
        print("Given node is not found in the list!!!")

    def display(self):
        if self.head is None:
            print("\nList is Empty!!!")
        else:
            print("\nList elements are:\n")
            print("NULL <--- ", end="")
            temp = self.head
            while True:
                print(f"{temp.data} <===> ", end="")
                temp = temp.next
                if temp == self.head:
                    break
            print("NULL")

# Driver code with menu
def menu():
    dll = DoublyCircularLinkedList()
    while True:
        print("\n*********** MENU *************")
        print("1. Insert\n2. Delete\n3. Display\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            while True:
                print("\nSelect from the following Inserting options")
                print("1. At Beginning\n2. At End\n3. After a Node\n4. Cancel")
                sub_choice = int(input("Enter your choice: "))
                if sub_choice == 1:
                    value = int(input("Enter the value to be inserted: "))
                    dll.insert_at_beginning(value)
                elif sub_choice == 2:
                    value = int(input("Enter the value to be inserted: "))
                    dll.insert_at_end(value)
                elif sub_choice == 3:
                    value = int(input("Enter the value to be inserted: "))
                    location = int(input("Enter the location after which you want to insert: "))
                    dll.insert_after(value, location)
                elif sub_choice == 4:
                    break
                else:
                    print("Please select correct Inserting option!!!")
        elif choice == 2:
            while True:
                print("\nSelect from the following Deleting options")
                print("1. At Beginning\n2. At End\n3. Specific Node\n4. Cancel")
                sub_choice = int(input("Enter your choice: "))
                if sub_choice == 1:
                    dll.delete_beginning()
                elif sub_choice == 2:
                    dll.delete_end()
                elif sub_choice == 3:
                    value = int(input("Enter the Node value to be deleted: "))
                    dll.delete_specific(value)
                elif sub_choice == 4:
                    break
                else:
                    print("Please select correct Deleting option!!!")
        elif choice == 3:
            dll.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Please select correct option!!!")
menu()
