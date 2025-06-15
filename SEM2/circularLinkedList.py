class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def insert_after(self, value, after_value):
        if not self.head:
            return
        temp = self.head
        while True:
            if temp.data == after_value:
                new_node = Node(value)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break

    def delete_beginning(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        self.head = self.head.next
        temp.next = self.head

    def delete_end(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        prev = None
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head

    def delete_specific(self, value):
        if not self.head:
            return
        curr = self.head
        prev = None
        while True:
            if curr.data == value:
                if curr == self.head and curr.next == self.head:
                    self.head = None
                elif curr == self.head:
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    self.head = self.head.next
                    temp.next = self.head
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            if curr == self.head:
                break

    def display(self):
        if not self.head:
            print("List is Empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()

def main():
    cll = CircularLinkedList()
    while True:
        print("\n1. Insert\n2. Delete\n3. Display\n4. Exit")
        choice1 = int(input("Enter choice: "))
        if choice1 == 1:
            while True:
                print("\n1. At Beginning\n2. At End\n3. After a Node\n4. Cancel")
                choice2 = int(input("Enter choice: "))
                if choice2 == 1:
                    value = int(input("Enter value: "))
                    cll.insert_at_beginning(value)
                elif choice2 == 2:
                    value = int(input("Enter value: "))
                    cll.insert_at_end(value)
                elif choice2 == 3:
                    value = int(input("Enter value: "))
                    after = int(input("Enter node value after which to insert: "))
                    cll.insert_after(value, after)
                elif choice2 == 4:
                    break
        elif choice1 == 2:
            while True:
                print("\n1. At Beginning\n2. At End\n3. Specific Node\n4. Cancel")
                choice2 = int(input("Enter choice: "))
                if choice2 == 1:
                    cll.delete_beginning()
                elif choice2 == 2:
                    cll.delete_end()
                elif choice2 == 3:
                    value = int(input("Enter node value to delete: "))
                    cll.delete_specific(value)
                elif choice2 == 4:
                    break
        elif choice1 == 3:
            cll.display()
        elif choice1 == 4:
            break

main()
