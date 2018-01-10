from tree import Node

def inOrder(treeNode, result):
    if treeNode is not None:
        inOrder(treeNode.leftNode, result)
        result.append(treeNode.data)
        inOrder(treeNode.rightNode, result)

def preOrder(treeNode, result):
    if treeNode is not None:
        result.append(treeNode.data)
        preOrder(treeNode.leftNode, result)
        preOrder(treeNode.rightNode, result)

def postOrder(treeNode, result):
    if treeNode is not None:
        postOrder(treeNode.leftNode, result)
        postOrder(treeNode.rightNode, result)
        result.append(treeNode.data)

def printInOrder(treeNode):
    arr = []
    inOrder(treeNode, arr)
    order = " -> ".join([str(item) for item in arr])
    print('In Order: ' + order)

def printPreOrder(treeNode):
    arr = []
    preOrder(treeNode, arr)
    order = " -> ".join([str(item) for item in arr])
    print('Pre Order: ' + order)

def printPostOrder(treeNode):
    arr = []
    postOrder(treeNode, arr)
    order = " -> ".join([str(item) for item in arr])
    print('Post Order: ' + order)