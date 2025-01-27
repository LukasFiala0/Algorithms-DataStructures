## Singly Linked List
class NodeSingle:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


node1 = NodeSingle(12)
node2 = NodeSingle(6)
node3 = NodeSingle(4)
node4 = NodeSingle(16)
node5 = NodeSingle(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


## Find the lowest value in Singly Linked List
def lowest_value(head:NodeSingle):
    min_val = head.data
    current_node = head.next
    while current_node:
        if current_node.data < min_val:
            min_val = current_node.data
        current_node = current_node.next
    return min_val

#print(lowest_value(node1))

## Delete a specific node in a Singly Linked List
def delete_node(head: NodeSingle, node_to_delete: NodeSingle):
    if head == None:
        return None
    if head == node_to_delete:
        new_head = head.next
        head.next = None
        return new_head
    current_node = head
    while current_node.next:
        if current_node.next == node_to_delete:
            current_node.next = current_node.next.next
            return head
        current_node = current_node.next
    return head

print("Before deleting:\n")

print_list(node1)

print("\n")

node1 = delete_node(node1, node3)

print("After deleting:\n")

print_list(node1)


def insert_node(head: NodeSingle, new_node: NodeSingle, position: int):
    if position <= 0:
        print("Invalid position!")
        return head

    if position == 1:
        new_node.next = head
        return new_node

    current_position = 1
    current_node = head

    while (current_position + 1) != position and current_node:
        current_position += 1
        current_node = current_node.next

    if current_node == None:
        print("Exceeded number of nodes!")
        return head

    new_node.next = current_node.next
    current_node.next = new_node

    return head



print("\n")

print("Before inserting:\n")

print_list(node1)

print("\n")

node_insert = NodeSingle(5555)
node1 = insert_node(node1, node_insert, 3)

print_list(node1)
