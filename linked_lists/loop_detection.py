from linked_list import LinkedList, Node

def loop_detection(linkedList):
    node = linkedList.head
    previousNodes = []

    while node is not None:
        for pn in previousNodes:
            if node is pn:
                print(node.data)
                return
        previousNodes.append(node)
        node = node.nextNode

linkedList = LinkedList()

aNode = Node('A', None)
bNode = Node('B', None)
cNode = Node('C', None)
dNode = Node('D', None)
eNode = Node('E', cNode)

linkedList.appendRawNodeToTail(aNode)
linkedList.appendRawNodeToTail(bNode)
linkedList.appendRawNodeToTail(cNode)
linkedList.appendRawNodeToTail(dNode)
linkedList.appendRawNodeToTail(eNode)

loop_detection(linkedList)