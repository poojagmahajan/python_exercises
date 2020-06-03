
## Implement Stack datastructure

class Stack :
    def __init__(self):
        self.items =[]

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items ==[]

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


myStack = Stack()
myStack.push("A")
myStack.push("B")
print(myStack.get_stack())
myStack.push(3)
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())
print(myStack.is_empty())
print(myStack.peek())
