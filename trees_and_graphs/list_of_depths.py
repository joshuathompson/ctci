from tree import Node

## Not using a linked list per the problem, but it's the same idea with an array

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

def build_depth_list(root, acc, depth=0):
    if root is not None:
        if acc.get(depth, None) is None:
            data = []
            data.append(root.data)
            acc[depth] = data
        else:
            acc[depth].append(root.data)
        build_depth_list(root.leftNode, acc, depth+1)
        build_depth_list(root.rightNode, acc, depth+1)

tree = build_minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
depth_list = {}
build_depth_list(tree, depth_list)
print(depth_list)