class CirculrDoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

node1 = CirculrDoubleNode(5)
node2 = CirculrDoubleNode(8)
node3 = CirculrDoubleNode(6)
node4 = CirculrDoubleNode(2)
node5 = CirculrDoubleNode(9)
node6 = CirculrDoubleNode(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node6.previous = node5
node5.previous = node4
node4.previous = node3
node3.previous = node2
node2.previous = node1

node6.next = node1
node1.previous = node6

print("\nTraversing forward:")
currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("...")

print("\nTraversing backward:")
currentNode = node4
startNode = node4
print(currentNode.data, end=" -> ")
currentNode = currentNode.previous

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.previous
print("...")
