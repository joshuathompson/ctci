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

def get_tree_elements(root, acc=[]):
    if root is not None:
        get_tree_elements(root.leftNode, acc)
        acc.append(root.data)
        get_tree_elements(root.rightNode, acc)

        return acc

    return acc

def first_common_ancestor(node, one, two, ancestors=[]):
    if node is not None:
        left_tree = get_tree_elements(node.leftNode, [])
        right_tree = get_tree_elements(node.rightNode, [])

        if (one in left_tree or one in right_tree) and (two in left_tree or two in right_tree):
            ancestors.append(node.data)

        first_common_ancestor(node.leftNode, one, two, ancestors)
        first_common_ancestor(node.rightNode, one, two, ancestors)

        return ancestors

    return ancestors

    
tree = build_minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
acc = first_common_ancestor(tree, 4, 1)
print(acc.pop())