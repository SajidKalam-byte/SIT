class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class d_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None 

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display(self):
        if not self.head:
            print("DOubly List is Empty")
            return
        print()
        temp = self.head
        while temp:
            print(f"{temp.data} <-> ", end="")
            temp = temp.next
        print("")

    def delete(self):
        if not self.head:
            print("Empty")
            return
        if not self.head.next:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

n = Node
obj = d_linked_list()
obj.insert(20)
obj.insert(12)
obj.insert(57)
obj.insert(55)
obj.insert(90)
obj.insert(28)
obj.insert(45)
obj.display()

obj.delete()
obj.display()