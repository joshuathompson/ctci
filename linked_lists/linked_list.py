class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

class LinkedList:
    def __init__(self):
        self.head = None

    def appendToTail(self, data):
        newNode = Node(data, None)

        if self.head is None:
            self.head = newNode
        else:
            node = self.head

            while node.nextNode is not None:
                node = node.nextNode

            node.nextNode = newNode

    def appendRawNodeToTail(self, newNode):

        if self.head is None:
            self.head = newNode
        else:
            node = self.head

            while node.nextNode is not None:
                node = node.nextNode
            
            node.nextNode = newNode

    def printList(self):
        allData = []

        node = self.head

        while node is not None:
            allData.append(str(node.data))
            node = node.nextNode

        print(" -> ".join(allData))