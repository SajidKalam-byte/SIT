class helloo:
    def __init__(self, size):
        self.size = size
        self.l = [0] * size
        self.rear = -1
        self.front = -1

    def enqueue(self, item):
        if self.rear == self.size - 1:
            print("Queue is full")
        else:
            self.rear = self.rear + 1
            self.l[self.rear] = item
            print("Pushed", item)
        if self.front == -1:
            self.front = 0
    def traverse(self):
        print("The items are: ", end=' ')
        for i in range(self.front, self.rear + 1, 1):
            print(self.l[i], end=" ")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            item = self.l[self.front]
            self.front = self.front + 1
            return item

size = input("Enter the Queue size: ")
obj = helloo(int(size))
while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Traverse\n4.Exit\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter the item: ")
        obj.enqueue(item)
    elif choice == "2":
        item = obj.dequeue()
        print("Popped", item)
    elif choice == "3":
        obj.traverse()
    elif choice == "4":
        break