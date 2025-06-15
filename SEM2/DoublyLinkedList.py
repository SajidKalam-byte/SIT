class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        print("Insertion success!!!")

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print("Insertion success!!!")

    def insert_after(self, value, location):
        if not self.head:
            self.insert_at_beginning(value)
            return
        temp = self.head
        while temp and temp.data != location:
            temp = temp.next
        if not temp:
            print("Given node is not found in the list!!!")
            return
        new_node = Node(value)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        print("Insertion success!!!")

    def delete_beginning(self):
        if not self.head:
            print("List is Empty!!! Deletion not possible!!!")
            return
        temp = self.head
        self.head = temp.next
        if self.head:
            self.head.prev = None
        del temp
        print("Deletion success!!!")

    def delete_end(self):
        if not self.head:
            print("List is Empty!!! Deletion not possible!!!")
            return
        temp = self.head
        if not temp.next:
            self.head = None
        else:
            while temp.next:
                temp = temp.next
            temp.prev.next = None
        del temp
        print("Deletion success!!!")

    def delete_specific(self, value):
        if not self.head:
            print("List is Empty!!! Deletion not possible!!!")
            return
        temp = self.head
        while temp and temp.data != value:
            temp = temp.next
        if not temp:
            print("Given node is not found in the list!!!")
            return
        if temp == self.head:
            self.head = temp.next
            if self.head:
                self.head.prev = None
        else:
            if temp.next:
                temp.next.prev = temp.prev
            temp.prev.next = temp.next
        del temp
        print("Deletion success!!!")

    def display(self):
        if not self.head:
            print("List is Empty!!!")
            return
        print("NULL <--- ", end="")
        temp = self.head
        while temp.next:
            print(f"{temp.data} <===> ", end="")
            temp = temp.next
        print(f"{temp.data} ---> NULL")

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            current_node.prev = next_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        print("List reversed!!!")

    def search(self, value):
        temp = self.head
        found = False
        while temp:
            if temp.data == value:
                found = True
                break
            temp = temp.next
        if found:
            print(f"{value} found in the list!!!")
        else:
            print(f"{value} not found in the list!!!")

dll = DoublyLinkedList()

while True:
    print("\n*********** MENU *************")
    print("1. Insert\n2. Delete\n3. Display\n4. Reverse\n5. Search\n6. Exit")
    choice1 = input("Enter your choice: ")
    
    if choice1 == '1':
        while True:
            print("\nSelect from the following Inserting options")
            print("1. At Beginning\n2. At End\n3. After a Node\n4. Cancel")
            choice2 = input("Enter your choice: ")
            if choice2 == '1':
                value = int(input("Enter value to insert at beginning: "))
                dll.insert_at_beginning(value)
            elif choice2 == '2':
                value = int(input("Enter value to insert at end: "))
                dll.insert_at_end(value)
            elif choice2 == '3':
                value = int(input("Enter value to insert: "))
                location = int(input("Enter the node value after which to insert: "))
                dll.insert_after(value, location)
            elif choice2 == '4':
                break
            else:
                print("Please select correct Inserting option!!!")
    elif choice1 == '2':
        while True:    
            print("\nSelect from the following Deleting options")
            print("1. At Beginning\n2. At End\n3. Specific Node\n4. Cancel")
            choice2 = input("Enter your choice: ")
            if choice2 == '1':
                dll.delete_beginning()
            elif choice2 == '2':
                dll.delete_end()
            elif choice2 == '3':
                value = int(input("Enter value to delete: "))
                dll.delete_specific(value)
            elif choice2 == '4':
                break
            else:
                print("Please select correct Deleting option!!!")
    elif choice1 == '3':
        dll.display()
    elif choice1 == '4':
        dll.reverse()
    elif choice1 == '5':
        value = int(input("Enter value to search: "))
        dll.search(value)
    elif choice1 == '6':
        break