from linked_list import LinkedList

def removeDuplicates(linkedList):
    if linkedList.head is None:
        return
        
    dataPoints = {}
    node = linkedList.head
    prevNode = None

    while node is not None:
        if dataPoints.get(node.data) is None:
            dataPoints[node.data] = True
        else:
            print("removed " + node.data)
            if node.nextNode is None:
                prevNode.nextNode = None
            else:
                prevNode.nextNode = node.nextNode

        prevNode = node
        node = node.nextNode

linkedList = LinkedList()
linkedList.appendToTail("1")
linkedList.appendToTail("2")
linkedList.appendToTail("2")
linkedList.appendToTail("3")
linkedList.appendToTail("1")
removeDuplicates(linkedList)
linkedList.printList()