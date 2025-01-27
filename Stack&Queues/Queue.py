## CREATING QUEUE USING ARRAYS

class QueueAR:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
            self.queue.append(item)

    def dequeue(self):
            if self.is_empty():
                return "Queue is empty"
            poped_item = self.queue.pop(0)
            return poped_item
        
    def peek(self):
            return self.queue[0]
        
    def is_empty(self):
            return self.queue == []
        
    def size(self):
            return len(self.queue)
        

# queue = QueueAR()
# print(queue.is_empty())
# queue.enqueue("yes")
# queue.enqueue("no")
# queue.enqueue(52)
# print(queue.peek())
# print(queue.is_empty())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.size())
# print(queue.dequeue())
# print(queue.is_empty())


## CREATING QUEUE USING SINGLY LINKED LIST 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLS:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.back == None:
            self.front = new_node
            self.back = new_node
            self.length += 1
            return
        self.back.next = new_node
        self.back = new_node
        self.length += 1
        
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        
        poped_item = self.front
        self.front = self.front.next
        self.length -= 1

        if self.front == None:
            self.back = None

        return poped_item.data
    
    def peek(self):
         return self.front.data
    
    def is_empty(self):
        return self.front == None
    
    def size(self):
        return self.length
    

# print("\n")

# queue = QueueLS()
# print(queue.is_empty())
# queue.enqueue("yes")
# queue.enqueue("no")
# queue.enqueue(52)
# print(queue.peek())
# print(queue.is_empty())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.size())
# print(queue.dequeue())
# print(queue.is_empty())