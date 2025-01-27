class NodeSingle:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = NodeSingle(12)
node2 = NodeSingle(7)
node3 = NodeSingle(5)

node1.next = node2
node2.next = node3

current_node = node1
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("null")
