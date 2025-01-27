class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('ROOT')
node_2 = TreeNode('2')
node_3 = TreeNode('3')
node_4 = TreeNode('4')
node_5 = TreeNode('5')
node_6 = TreeNode('6')
node_7 = TreeNode('7')

# NODE_2 SUBTREE
root.left = node_2
node_2.left = node_4
node_2.right = node_5

# NODE_3 SUBTREE
root.right = node_3
node_3.left = node_6
node_3.right = node_7

# Test
#print("root.right.left.data:", root.right.left.data)


### DEPTH FIRST SEARCH - PRE-ORDER TRAVERSAL
def pre_order_traversal(node: TreeNode):
    if node == None:
        print("None")
        return
    # process the node ~ print it
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

#pre_order_traversal(root)


### DEPTH FIRST SEARCH - IN-ORDER TRAVERSAL
def in_order_traversal(node: TreeNode):
    if node == None:
        print("None")
        return
    in_order_traversal(node.left)
    # process the node ~ print it
    print(node.data)
    in_order_traversal(node.right)

#in_order_traversal(root)


### DEPTH FIRST SEARCH - POST-ORDER TRAVERSAL
def post_order_traversal(node: TreeNode):
    if node == None:
        print("None")
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    # process the node ~ print it
    print(node.data)

#post_order_traversal(root)
