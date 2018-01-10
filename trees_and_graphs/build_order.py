from graph import Graph, Node

def build_graph(projects, dependencies):
    graph = Graph()
    nodes = []
    for p in projects:
        nodes.append(Node(p))

    for d in dependencies:
        origin_name = d[0]
        destination_name = d[1]

        origin_index = -1
        destination_index = -1

        for index, n in enumerate(nodes):
            if n.data == origin_name:
                origin_index = index
            elif n.data == destination_name:
                destination_index = index
        
        if origin_index != -1 and destination_index != -1:
            nodes[origin_index].children.append(nodes[destination_index])

    graph.children = nodes

    return graph

def travel_graph(node):
    acc = []
    queue = []
    node.marked = True
    queue.insert(0, node)

    while len(queue) > 0:
        node = queue.pop()

        for child in node.children:
            if child.data not in acc:
                acc.append(child.data)
                queue.insert(0, child)

    return acc


def find_build_order(graph, projects):
    deps = set()
    for node in graph.children:
        acc = set(travel_graph(node))

        deps = deps.union(acc)

    no_deps = set(projects).difference(set(deps))

    result = list(no_deps) + list(deps)
    
    if len(result) == len(projects):
        return result
    else:
        return "No Valid Build"

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
g = build_graph(projects, dependencies)
print(find_build_order(g, projects))