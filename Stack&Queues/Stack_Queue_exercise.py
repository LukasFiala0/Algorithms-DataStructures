from Queue import QueueLS, QueueAR
from Stack import StackLS, StackAR


## Valid Parentheses
def valid_parentheses(parentheses:str):
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}"
        }
    stack = StackAR()
    for char in parentheses:
        if char in brackets.keys():
            stack.push(char)
        elif char in brackets.values():
            if stack.isEmpty():
                return False
            check = stack.peek()
            if brackets[check] == char:
                stack.pop()
            else:
                return False
            

    return stack.isEmpty()
    
#print(valid_parentheses("[{()]}"))


## Collapse string
def collapse_string(string:str):
    stack = StackLS()
    result = []
    for char in string:
        stack.push(char)
    while not stack.is_empty():   # while stack.head
        result.append(stack.pop())  #result += stack.pop()
    
    return ''.join(result)

print(collapse_string("hello"))


## Reverse first K elements in queue
queue = QueueAR()
queue.enqueue(5)
queue.enqueue(8)
queue.enqueue(2)
queue.enqueue(1)
queue.enqueue(4)
queue.enqueue(7)

def reverse_queue(queue: QueueAR, k:int):
    if k > queue.size() or k <= 0:
        return "invalid input of k"

    help_stack = []

    for i in range(k):
        help_stack.append(queue.dequeue())

    while help_stack:
          queue.enqueue(help_stack.pop())

    left_k = queue.size() - k
    for j in range(left_k):
          queue.enqueue(queue.dequeue())

    return queue
#print(reverse_queue(queue, 4).queue)


## Generating first N binary numbers
def binary_nums(n:int):
    result = []
    queue = QueueLS()
    queue.enqueue("1")
    for i in range(n):
        current = queue.dequeue()
        result.append(current)
        queue.enqueue(current + "0")
        queue.enqueue(current + "1")
   
    return result

#print(binary_nums(5))









