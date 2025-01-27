class CircularSingleNode:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = CircularSingleNode(3)
node2 = CircularSingleNode(8)
node3 = CircularSingleNode(6)
node4 = CircularSingleNode(2)
node5 = CircularSingleNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node5.next = node1

print("\nTraversing\n")
start = node1

for i in range(11):
    print(start.data, end=" -> ")    
    start = start.next