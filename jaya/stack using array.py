class StackUsingArray:
      def __init__(self):
            self.stack = [ ]
      def push(self,element):
          self.stack.append(element)
      def pop(self):
            if(not self.isEmpty()):
                  lastElement = self.stack[-1]
                  del(self.stack[-1])
                  return lastElement
            else:
                return("stack already empty")
      def isEmpty(self):
             return self.stack ==[ ]
      def printStack(self):
             print(self.stack)
s = StackUsingArray( )
print("*"*5+" Stack using Array""*****")
while True:
      el = int(input("1 for Push\n2 for pop\n3 to check if it is Empty\n4 to print Stack\n5 to exit\n"))
      if(el == 1):
             item = int(input("Enter element to push in stack:\n"))        
             s.push(item)
      if(el == 2):
             print(s.pop())
      if(el == 3):
             print(s.isEmpty ( ))
      if(el == 4):
             s.printStack()
      if(el == 5):
             break           
                        
                        
