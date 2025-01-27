class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order_traversal(node:TreeNode):
    if node == None:
        return None
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)

### 1.) CREATE A BST FROM THESE VALUES:
values = [50, 30, 70, 20, 40, 60, 80]

def insert(node:TreeNode, new_node:TreeNode):
    if node == None:
        return new_node
    else:
        if new_node.data > node.data:
            node.right = insert(node.right, new_node)
        elif new_node.data < node.data:
            node.left = insert(node.left, new_node)
    return node

def create_BST(nodes:list):
    root = TreeNode(nodes[0])
    for i in range(1,len(nodes)):
        insert(root, TreeNode(nodes[i]))
    return root

root = create_BST(values)
#in_order_traversal(root)

### CREATE FUNCTION FOR SEARCHING A NODE WITH VALLUE
def search(node:TreeNode, value:int):
    if node == None:
        return None
    
    elif node.data == value:
        return node
    else:
        if value > node.data:
            return search(node.right, value)
        elif value < node.data:
            return search(node.left, value)


### FIND MAXIMUM AND MINIMUN VALUES 
def minimum(node:TreeNode):
    if node is None:
        return None
    
    if node.left == None:
        return node
    return minimum(node.left)

def maximum(node:TreeNode):
    if node.right == None:
        return node
    return maximum(node.right)

def min_max(node:TreeNode):
    return (minimum(node).data, maximum(node).data)


### OR...
def min_max(node: TreeNode):
    if node is None:
        return None
    
    min_node = node
    max_node = node
    
    while min_node.left is not None:
        min_node = min_node.left
    
    while max_node.right is not None:
        max_node = max_node.right
    
    return (min_node.data, max_node.data)

### CALCULATING THE HEIGHT OF THE TREE
def height_tree(node:TreeNode):
    if node == None:
        return -1
    
    lowest_node = height_tree(node.left)
    highest_node = height_tree(node.right)

    return max(lowest_node, highest_node) + 1

# tree_height = height_tree(root)
# print(f"Výška stromu je: {tree_height}")


### K-th SMALLEST ELEMENT IN BST
def k_smallest(node, k, counter):
    if node == None:
        return None

    left_result = k_smallest(node.left, k, counter)
    if left_result is not None:
        return left_result

    counter[0] += 1      # counter has to be a mutable object
    if counter[0] == k:
        return node.data

    return k_smallest(node.right, k, counter)

#print(k_smallest(root, 5, counter= [0]))


### SIZE OF A BST
def size_BST(node:TreeNode):
    if node == None:
        return 0
    
    left = size_BST(node.left)
    right = size_BST(node.right)

    return  left + right + 1


#print(size_BST(root))