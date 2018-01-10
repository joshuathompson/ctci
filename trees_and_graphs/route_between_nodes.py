from graph import Graph, Node

def route_between_nodes(start, destination):
    queue = []
    start.marked = True
    queue.insert(0, start)

    while len(queue) > 0:
        node = queue.pop()

        for child in node.children:
            if child.marked == False:
                if child.data == destination.data:
                    return True
                child.marked = True
                queue.insert(0, child)

    return False



graph = Graph()

zeroNode = Node('0')
oneNode = Node('1')
twoNode = Node('2')
threeNode = Node('3')
fourNode = Node('4')
fiveNode = Node('5')
sixNode = Node('6')

zeroNode.children.append(oneNode)
zeroNode.children.append(fourNode)
zeroNode.children.append(fiveNode)

oneNode.children.append(threeNode)
oneNode.children.append(fourNode)

twoNode.children.append(oneNode)

threeNode.children.append(twoNode)
threeNode.children.append(fourNode)

graph.nodes.append(zeroNode)
graph.nodes.append(sixNode)

print(route_between_nodes(zeroNode, twoNode))
print(route_between_nodes(zeroNode, sixNode))