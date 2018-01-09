from linked_list import LinkedList

def removeKthToLast(linkedList, k):
    node = linkedList.head
    length = 0

    while node is not None:
        node = node.nextNode
        length += 1

    if length == 0 or k > length:
        return #empty

    elementToRemove = length - k
    currentIndex = 0

    node = linkedList.head
    prevNode = None

    while currentIndex < elementToRemove:
        prevNode = node
        node = node.nextNode
        currentIndex += 1

    if prevNode is None:
        linkedList.head = linkedList.head.nextNode
    else:
        prevNode.nextNode = node.nextNode
    
    return

linkedList = LinkedList()
linkedList.appendToTail("1")
linkedList.appendToTail("2")
linkedList.appendToTail("3")
linkedList.appendToTail("4")
linkedList.appendToTail("5")
removeKthToLast(linkedList, 3)
linkedList.printList()