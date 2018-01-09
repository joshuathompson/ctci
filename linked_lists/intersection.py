from linked_list import LinkedList, Node

def intersection(linkedListOne, linkedListTwo):
    savedNodes = []
    node = linkedListOne.head

    while node is not None:
        savedNodes.append(node)
        node = node.nextNode

    node = linkedListTwo.head

    while node is not None:
        for sn in savedNodes:
            if sn is node:
                print(node.data)
                return

        node = node.nextNode

    print("No match")
    return

linkedListOne = LinkedList()

aNode = Node('A', None)
bNode = Node('B', None)
cNode = Node('C', None)
dNode = Node('D', None)
eNode = Node('E', None)

linkedListOne.appendRawNodeToTail(aNode)
linkedListOne.appendRawNodeToTail(bNode)
linkedListOne.appendRawNodeToTail(cNode)
linkedListOne.appendRawNodeToTail(dNode)
linkedListOne.appendRawNodeToTail(eNode)

linkedListTwo = LinkedList()

fNode = Node('F', None)
gNode = Node('G', None)
hNode = Node('H', None)
iNode = Node('I', dNode)

linkedListTwo.appendRawNodeToTail(fNode)
linkedListTwo.appendRawNodeToTail(gNode)
linkedListTwo.appendRawNodeToTail(hNode)
linkedListTwo.appendRawNodeToTail(iNode)

intersection(linkedListOne, linkedListTwo)