class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = self.size = 0
        self.rear = capacity - 1
        self.queue = [None] * capacity
    
    def is_full(self):
        return self.size == self.capacity
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements are:", end=' ')
        for i in range(self.front, self.front + self.size):
            print(self.queue[i % self.capacity], end=' ')
        print()

# Example usage
my_queue = Queue(5)

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)

my_queue.print_queue()  # Should print "Queue elements are: 1 2 3 4 5"

print(my_queue.dequeue())  # Should print 1
print(my_queue.dequeue())  # Should print 2

my_queue.print_queue()  # Should print "Queue elements are: 3 4 5"
