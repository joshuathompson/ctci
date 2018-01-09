from linked_list import LinkedList

def build_number_from_list(linkedList):
    node = linkedList.head
    
    numbers = []
    while node is not None:
        numbers.append(node.data)
        node = node.nextNode

    result = 0
    numbers.reverse()
    for num in numbers:
        result = (result*10) + num

    return result

def sum_lists(listOne, listTwo):
    numOne = build_number_from_list(listOne)
    numTwo = build_number_from_list(listTwo)
    sumNum = numOne + numTwo

    returnList = LinkedList()
    
    while sumNum != 0:
        quotient = sumNum / 10
        remainder = sumNum % 10
        
        returnList.appendToTail(remainder)
        sumNum = quotient
    
    return returnList

def build_number_from_list_forward(linkedList):
    node = linkedList.head
    
    numbers = []
    while node is not None:
        numbers.append(node.data)
        node = node.nextNode

    result = 0
    for num in numbers:
        result = (result*10) + num

    return result

def sum_lists_forward(listOne, listTwo):
    numOne = build_number_from_list_forward(listOne)
    numTwo = build_number_from_list_forward(listTwo)
    sumNum = numOne + numTwo

    returnList = LinkedList()
    
    while sumNum != 0:
        quotient = sumNum / 10
        remainder = sumNum % 10
        
        returnList.appendToTail(remainder)
        sumNum = quotient
    
    return returnList



linkedListOne = LinkedList()
linkedListOne.appendToTail(7)
linkedListOne.appendToTail(1)
linkedListOne.appendToTail(6)

linkedListTwo = LinkedList()
linkedListTwo.appendToTail(5)
linkedListTwo.appendToTail(9)
linkedListTwo.appendToTail(2)

rtnList = sum_lists(linkedListOne, linkedListTwo)
rtnList.printList()

linkedListOne = LinkedList()
linkedListOne.appendToTail(6)
linkedListOne.appendToTail(1)
linkedListOne.appendToTail(7)

linkedListTwo = LinkedList()
linkedListTwo.appendToTail(2)
linkedListTwo.appendToTail(9)
linkedListTwo.appendToTail(5)

rtnList = sum_lists_forward(linkedListOne, linkedListTwo)
rtnList.printList()