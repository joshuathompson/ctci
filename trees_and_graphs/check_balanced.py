from tree import Node
import math

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

def find_max_depth(root, depth=0):
    if root is not None:
        depth_left = find_max_depth(root.leftNode, depth+1)
        depth_right = find_max_depth(root.rightNode, depth+1)

        if depth_left > depth_right:
            return depth_left
        else:
            return depth_right
    
    return depth

def check_balanced(root):
    if root is not None:
        depth_right = find_max_depth(root.rightNode)
        depth_left = find_max_depth(root.leftNode)

        if math.fabs(depth_right - depth_left) > 1:
            return False

        check_left = check_balanced(root.leftNode)
        check_right = check_balanced(root.rightNode)

        return check_left and check_right

    return True

tree = build_minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(check_balanced(tree))

tree.leftNode.leftNode.leftNode.leftNode = Node(22)
print(check_balanced(tree))