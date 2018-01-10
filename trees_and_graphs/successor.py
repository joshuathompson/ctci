from tree import Node

def build_minimal_tree(numbers):
    if len(numbers) > 1:
        mid_point = len(numbers)/2
        left_tree = numbers[:mid_point]
        right_tree = numbers[mid_point+1:] 

        root = Node(numbers[mid_point])
        root.leftNode = build_minimal_tree(left_tree)
        root.rightNode = build_minimal_tree(right_tree)
        return root
    elif len(numbers) == 1:
        return Node(numbers[0])
    else:
        return None

def find_successor_node(node, target):
    if node is not None:
        lower_val = find_successor_node(node.leftNode, target)
        higher_val = find_successor_node(node.rightNode, target)

        if lower_val - target > 0:
            return lower_val

        if node.data - target > 0:
            return node.data

        if higher_val - target > 0:
            return higher_val

        return -1
    
    return -1

target = 7
tree = build_minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
acc = find_successor_node(tree, target)
print(acc)