from linked_list import LinkedList

def partition(linkedList, pValue):
    if linkedList.head is None:
        return

    node = linkedList.head
    prevNode = None
    nodesToReattach = []

    while node is not None:
        if node.data >= pValue:
            if prevNode is None:
                linkedList.head = node.nextNode
            else:
                prevNode.nextNode = node.nextNode
            nodesToReattach.append(node)
            node = node.nextNode
        else:
            prevNode = node
            node = node.nextNode

    for nodeToAttach in nodesToReattach:
        nodeToAttach.nextNode = None # remove old refernece or else we're circular
        prevNode.nextNode = nodeToAttach
        prevNode = nodeToAttach
    

linkedList = LinkedList()
linkedList.appendToTail(3)
linkedList.appendToTail(5)
linkedList.appendToTail(8)
linkedList.appendToTail(5)
linkedList.appendToTail(10)
linkedList.appendToTail(2)
linkedList.appendToTail(1)
partition(linkedList, 5)
linkedList.printList()