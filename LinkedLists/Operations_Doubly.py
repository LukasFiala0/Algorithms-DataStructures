class NodeDouble:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

def print_list_forward(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def print_list_backward(tail):
    current = tail
    while current:
        print(current.data, end=" -> ")
        current = current.previous
    print("None")

node1 = NodeDouble(1)
node2 = NodeDouble(8)
node3 = NodeDouble(5)
node4 = NodeDouble(9)
node5 = NodeDouble(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node5.previous = node4
node4.previous = node3
node3.previous = node2
node2.previous = node1


## FIND THE LOWEST VALUE in Doubly linked list (Backward..)
def highest_value(tail:NodeDouble):
    if tail == None:
        return "Empty list"
    min_val = tail.data
    current_node = tail
    while current_node.previous:
        if current_node.previous.data > min_val:
            min_val = current_node.previous.data
        else:
            current_node = current_node.previous
    return min_val

print(f"The highest value is {highest_value(node5)}")

## DELETE A NODE ON A SPECIFIC POSITION
def delete_node(head, position):
    if head == None:
        print("Empty list")
        return None

    if position <= 0:
        print("Invalid position!")
        return head
    
    if position == 1:
        new_head = head.next
        head.next = None
        if new_head:
            new_head.previous = None
        return new_head
    
    current_position = 2
    current_node = head.next
    while current_position != position and current_node:
        current_position += 1
        current_node = current_node.next
    if current_node == None:
        print("Exceeded number of nodes!")
        return head    
    
    current_node.previous.next = current_node.next

    if current_node.next:
        current_node.next.previous = current_node.previous
    
    current_node = None
    return head

# This code doesnt solve the rest reference, try "print_list_backwards"    
print("\nBefore Deleting")
print_list_forward(node1)

head = delete_node(node1, 5)

print("\nAfter Deleting")
print_list_forward(head)

## INSERT A NODE AFTER A SPECIFIC NODE:
def insert_node_after(head: NodeDouble, new_node:NodeDouble, spec_node:NodeDouble):
    if head == None:
        print("Empty list")
        return None

    if new_node is None or spec_node is None:
        print("Invalid given nodes")
        return head
    
    current_node = head

    while current_node != spec_node and current_node:
        current_node = current_node.next

    if current_node is None:
        print("Specified node not found in the list.")
        return head
    
    if current_node.next:
        current_node.next.previous = new_node
    new_node.next = current_node.next
    new_node.previous = current_node
    current_node.next = new_node

    return head

new_node = NodeDouble(555)
head = insert_node_after(node1, new_node, node4)
print_list_forward(head)






















