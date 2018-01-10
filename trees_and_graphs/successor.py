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

def find_successor_node(node, acc=[]):
    if node is not None:
        find_successor_node(node.leftNode, acc)
        acc.append(node.data)
        find_successor_node(node.rightNode, acc)

        return acc
    
    return acc

target = 7
tree = build_minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
acc = find_successor_node(tree)

for index, num in enumerate(acc):
    if num == target:
        if index == len(acc)-1:
            print("None")
        else:
            print(acc[index+1])