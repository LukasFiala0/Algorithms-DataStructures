binary_tree_array = ['R', '2', '3', '4', '5', '6', '7']   # A perfect binary tree, if non-BT -> arange indices

def left_child_index(index):
    return 2 * index + 1

def right_child_index(index):
    return 2 * index + 2

def get_data(index):
    if 0 <= index < len(binary_tree_array):
        return binary_tree_array[index]
    return None


right_child = right_child_index(0)
left_child_of_right_child = left_child_index(right_child)
data = get_data(left_child_of_right_child)

print("root.right.left.data:", data)

### DEPTH FIRST SEARCH - PRE-ORDER TRAVERSAL
def pre_order_traversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] == None:   #second condition for non-perfect BT
        return []
    return [binary_tree_array[index]] + pre_order_traversal(left_child_index(index)) + pre_order_traversal(right_child_index(index))
    
#print(pre_order_traversal(0))

### DEPTH FIRST SEARCH - IN-ORDER TRAVERSAL
def in_order_traversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] == None:   #second condition for non-perfect BT
        return []
    return  in_order_traversal(left_child_index(index)) + [binary_tree_array[index]] + in_order_traversal(right_child_index(index))

#print(in_order_traversal(0))

### DEPTH FIRST SEARCH - POST-ORDER TRAVERSAL
def post_order_traversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] == None:   #second condition for non-perfect BT
        return []
    return  post_order_traversal(left_child_index(index)) + post_order_traversal(right_child_index(index)) + [binary_tree_array[index]]

#print(post_order_traversal(0))