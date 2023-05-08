class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def add_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def remove_front(self):
        if self.is_empty():
            print("List is empty")
        else:
            self.head = self.head.next
    
    def remove_back(self):
        if self.is_empty():
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
    
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

# Example usage
my_list = SinglyLinkedList()

my_list.add_front(1)
my_list.add_front(2)
my_list.add_front(3)
my_list.add_back(4)
my_list.add_back(5)

my_list.print_list()  # Should print "3 2 1 4 5"

my_list.remove_front()
my_list.remove_back()

my_list.print_list()  # Should print "2 1 4"

print(my_list.search(1))  # Should print True
print(my_list.search(5))  # Should print False
