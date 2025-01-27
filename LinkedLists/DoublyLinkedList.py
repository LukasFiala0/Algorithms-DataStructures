class NodeDouble:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

node1 = NodeDouble(4)
node2 = NodeDouble(8)
node3 = NodeDouble(11)
node4 = NodeDouble(9)

node1.next = node2
node2.next = node3
node3.next = node4

node4.previous = node3
node3.previous = node2
node2.previous = node1

print("\n forward Traversing:\n")
current_node = node1
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("null")

print("\n backward Traversing")
current_node = node4
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.previous
print("null")