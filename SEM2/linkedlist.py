class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def InsertBeginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            
            new_node.next = self.head
            self.head = new_node
        print("\nNode inserted at the beginning of the linked list.")

    def InsertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print("\nNode inserted at the end of the linked list.")

    def InsertSpecified(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(position - 1):
                if temp.next is None:
                    print("\nPosition out of range.")
                    return
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        print("\nNode inserted at specified position.")

    def Deletehead(self):
        if self.head is None:
            print("\nLinked list is empty.")
        else:
            self.head = self.head.next
            print("\nNode deleted from the head of the linked list.")

    def DeleteEnd(self):
        if self.head is None:
            print("\nLinked list is empty.")
        elif self.head.next is None:
            self.head = None
            print("\nNode deleted from the end of the linked list.")
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            print("\nNode deleted from the end of the linked list.")

    def DeleteSpecified(self, position):
        if position == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(position - 1):
                if temp.next is None:
                    print("\nPosition out of range.")
                    return
                temp = temp.next
            if temp.next is None:
                print("\nPosition out of range.")
            else:
                temp.next = temp.next.next
        print("\nNode deleted from specified position.")

    def traverse(self):
        if self.head is None:
            print("\nLinked list is empty.")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def Reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("\nLinked list reversed.")

    def Search(self, data):
        temp = self.head
        found = False
        while temp is not None:
            if temp.data == data:
                found = True
                break
            temp = temp.next
        if found:
            print("\nElement found in the linked list.")
        else:
            print("\nElement not found in the linked list.")

ll = LinkedList()
while True:
    print("\n1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at specified position")
    print("4. Delete from head")
    print("5. Delete from end")
    print("6. Delete from specified position")
    print("7. Traverse")
    print("8. Reverse")
    print("9. Search")
    print("10. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to insert: "))
        ll.InsertBeginning(data)
    elif choice == 2:
        data = int(input("Enter data to insert: "))
        ll.InsertEnd(data)
    elif choice == 3:
        data = int(input("Enter data to insert: "))
        position = int(input("Enter position to insert: "))
        ll.InsertSpecified(data, position)
    elif choice == 4:
        ll.Deletehead()
    elif choice == 5:
        ll.DeleteEnd()
    elif choice == 6:
        position = int(input("Enter position to delete: "))
        ll.DeleteSpecified(position)
    elif choice == 7:
        ll.traverse()
    elif choice == 8:
        ll.Reverse()
    elif choice == 9:
        data = int(input("Enter data to search: "))
        ll.Search(data)
    elif choice == 10:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

    print()
