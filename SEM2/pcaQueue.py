class CQueue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.list =[0] * size

    def enqueue(self, item):
        if self.rear == self.size -1:
            print("CQueue is full")
        else:
            print("Rear :", self.rear)
            self.rear = (self.rear +1) % self.size
            print("Rear +:", self.rear)
            self.list[self.rear] = item
            print("Enqueue ", item)
            if self.front == -1:
                self.front = (self.front +1)
    
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            item = self.list[self.front]
            print("Front: ", self.front)
            self.front = (self.front +1)  % self.size
            print("Front++: ", self.front)
            return item
        if self.front== self.rear:
            self.front=self.rear = -1
        
    # def traverse(self):
    #     print("The items are: ", end=' ')
    #     for i in range(self.front, self.rear+1, 1):
    #         print(self.list[i], end=' ')


obj = CQueue(4)
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
print("Dequeue: ",obj.dequeue())
print("Dequeue: ",obj.dequeue())
print("Dequeue: ",obj.dequeue())
print("Dequeue: ",obj.dequeue())

# obj.traverse()
