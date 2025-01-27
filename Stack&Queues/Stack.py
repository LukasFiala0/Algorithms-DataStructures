## CREATING STACK USING ARRAYS

class StackAR:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


# myStack = StackAR()
# myStack.push('A')
# myStack.push('B')
# myStack.push('C')
# print(myStack.stack)
# print(myStack.pop())
# print(myStack.peek())
# print(myStack.isEmpty())
# print(myStack.size())


## CREATING STACK USING SINGLY LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLS:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, item):  # the head is always on top of the stack and pointing to previous one
        new_node = Node(item)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        poped_item = self.head
        self.head = self.head.next
        self.size -= 1
        return poped_item.data
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.head.data
    
    def is_empty(self):
        if self.size == 0:
            return True
        return False
    
    def stack_size(self):
        return self.size
    

# my_stack = StackLS()
# print(my_stack.is_empty())
# my_stack.push(12)
# my_stack.push('String')
# my_stack.push(8.654)
# print(my_stack.peek())
# print(my_stack.is_empty())
# print(my_stack.pop())
# print(my_stack.stack_size())
