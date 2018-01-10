from tree import Node
from traversal import printInOrder, printPreOrder, printPostOrder

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

tree = build_minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
printInOrder(tree)
printPreOrder(tree)
printPostOrder(tree)