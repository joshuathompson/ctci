from linked_list import LinkedList

def deleteMiddleNode(linkedList):
    length = 0

    node = linkedList.head

    while node is not None:
        length += 1
        node = node.nextNode

    middle = length/2

    node = linkedList.head
    prevNode = None
    i = 0

    while node is not None:
        if i == middle:
            prevNode.nextNode = node.nextNode
            node = None
        else:
            prevNode = node
            node = node.nextNode
            i += 1

linkedList = LinkedList()
linkedList.appendToTail("1")
linkedList.appendToTail("2")
linkedList.appendToTail("3")
linkedList.appendToTail("4")
linkedList.appendToTail("5")
deleteMiddleNode(linkedList)
linkedList.printList()