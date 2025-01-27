# A Binary Search Tree (BST) is a type of Binary Tree data structure, where the following properties must be true for any node "X" in the tree:

# The X node's left child and all of its descendants (children, children's children, and so on) have lower values than X's value.
# The right child, and all its descendants have higher values than X's value.
# Left and right subtrees must also be Binary Search Trees.

# These properties makes it faster to search, add and delete values than a regular binary tree.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

### DEPTH FIRST SEARCH - IN-ORDER TRAVERSAL   ~ ~ SORTING ALGORITHM
def in_order_traversal(node: TreeNode):
    if node == None:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)

root = TreeNode(16)
node2 = TreeNode(8)
node3  = TreeNode(23)
node4 = TreeNode(6)
node5 = TreeNode(12)
node6 = TreeNode(18)
node7 = TreeNode(25)
node8 = TreeNode(3)
node9 = TreeNode(24)

root.left = node2
node2.left = node4
node2.right = node5
node4.left = node8
root.right = node3
node3.left = node6
node3.right = node7
node7.left = node9

#in_order_traversal(root)

### SEARCH FOR A VALUE in BST
def search(node:TreeNode, value):
    if node == None:
        return "Error"
    if node.data == value:
        return node
    if node.data >= value:
        return search(node.left, value)
    if node.data <= value:
        return search(node.right, value)


#print(search(root, 18))

#The time complexity for searching a BST for a value is O(h), where h is the height of the tree.
# We can obtain the same result from balanced and unbalanced BST!! But with different time complexity --> INTRODUCE AVL TREES


### INSERTING A NODE into BST  --- NOT BALANCED
def insert(node:TreeNode, new_node:TreeNode):
    if node == None:
        return new_node
    else:
        if node.data > new_node.data:
            node.left = insert(node.left, new_node)
        elif node.data < new_node.data:
            node.right = insert(node.right, new_node)
    return node

# node = insert(root, TreeNode(20))
# print(in_order_traversal(node))

### FIND THE LOWEST VALUE:
def lowest_value(node:TreeNode):
    if node.left == None:
        return node.data
    return lowest_value(node.left)

#print(lowest_value(root))

### DELETE A NODE:
def delete(node:TreeNode, node_to_delete:TreeNode):
    if node == None:
        return None
    # searching for the node that is the node_to_delete
    if node.data > node_to_delete.data:
        node.left = delete(node.left, node_to_delete)
    elif node.data < node_to_delete.data:
        node.right = delete(node.right, node_to_delete)
    # node is now the node_to_delete
    else:
        if node.right == None:   #the node has only one LEFT child or zero child
            temp = node.left
            node = None
            return temp
        elif node.left == None:     #the node has only one RIGHT child or zero child
            temp = node.right
            node = None
            return temp
        else:                   # the node has both child
            node.data = lowest_value(node.right)   # node.right is also accpetable?
            node.right = delete(node.right, node)

    return node


# node = delete(root, node8)
# in_order_traversal(node)