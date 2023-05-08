class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements are:", end=' ')
        for item in self.queue:
            print(item, end=' ')
        print()
my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)

my_queue.print_queue()  # Should print "Queue elements are: 1 2 3 4 5"

print(my_queue.dequeue())  # Should print 1
print(my_queue.dequeue())  # Should print 2

my_queue.print_queue()  # Should print "Queue elements are: 3 4 5"
