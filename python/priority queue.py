class priorityqueue:
    def __init__(self):
        self.queue=[]
    def is_empty(self):
        return len(self.queue)==0
    def enqueue(self,element,priority):
        self.queue.append((element,priority))
        self.queue=sorted(self.queue,key=lambda x:x[1],reverse=True)
    def dequeue(self):
        if self.is_empty():
            print("priority queue is empty. Dequeue operation is failed")
            return None
        else:
            item=self.queue.pop(0)
            return item[0]
    def display(self):
        if self.is_empty():
            print("priority queue is empty")
        else:
            print("priority queue elements by priority:")
            for item in self.queue:
                print("element:",item[0],"priority:",item[1])

pq=priorityqueue()
pq.enqueue("task1",3)
pq.enqueue("task2",1)
pq.enqueue("task3",2)
pq.enqueue("task4",4)
pq.display()
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.is_empty())
