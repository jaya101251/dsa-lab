class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1
    
    def is_empty(self):
        return self.head == -1
    
    def is_full(self):
        return (self.tail + 1) % self.k == self.head
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
        elif self.is_empty():
            self.head = 0
            self.tail = 0
            self.queue[0] = item
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = item
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        elif self.head == self.tail:
            item = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return item
        else:
            item = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return item
q = CircularQueue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue()) 
print(q.dequeue())
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())  
print(q.dequeue())  
print(q.dequeue()) 
