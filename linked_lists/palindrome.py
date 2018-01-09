from linked_list import LinkedList

def is_palindrome(linkedList):
    palindromeStr = ""
    node = linkedList.head

    while node is not None:
        palindromeStr += node.data
        node = node.nextNode

    palindromeStr = palindromeStr.replace(" ", "")
    reversedPalindrome = palindromeStr[::-1]

    return palindromeStr == reversedPalindrome

linkedList = LinkedList()
linkedList.appendToTail('r')
linkedList.appendToTail('a')
linkedList.appendToTail('c')
linkedList.appendToTail('e')
linkedList.appendToTail('c')
linkedList.appendToTail('a')
linkedList.appendToTail('r')
print(is_palindrome(linkedList))

linkedList = LinkedList()
linkedList.appendToTail('r')
linkedList.appendToTail('a')
linkedList.appendToTail('w')
linkedList.appendToTail('r')
print(is_palindrome(linkedList))
