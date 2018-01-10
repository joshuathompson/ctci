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

def validate_bst(root):
    if root is not None:
        if root.leftNode is not None and root.data < root.leftNode.data:
            return False

        if root.rightNode is not None and root.data > root.rightNode.data:
            return False

        left_good = validate_bst(root.leftNode)
        right_good = validate_bst(root.rightNode)

        return left_good and right_good

    return True

tree = build_minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
valid = validate_bst(tree)
print(valid)