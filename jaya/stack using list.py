class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        return self.head is None
    def push(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def pop(self):
        if self.isempty():
            return None
        else:
            popped_node=self.head
            self.head=self.head.next
            popped_node.next= None
            return popped_node.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        if self.head is None:
            print("stack underflow")
        else:
            current=self.head
            while current is not None:
                print(current.data)
                current=current.next

newstack=stack()
newstack.push(10)
newstack.push(12)
newstack.push(13)
newstack.push(14)
newstack.display()
print("\n top element is:",newstack.peek())
newstack.pop()
newstack.pop()
newstack.display()
print("\n top element is:",newstack.peek())
