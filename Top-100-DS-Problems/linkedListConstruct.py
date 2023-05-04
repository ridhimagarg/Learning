
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def setHead(self, node):
        pass

    def setTail(self, node):
        pass

    def insertBefore(self, node, nodeToInsert):
        pass

    def insertAfter(self, node, nodeToInsert):
        pass

    def insertAtPosition(self, position, nodeToInsert):
        pass

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                self.remove(value)

    def remove(self, node):
        ## we have to check here for the edge cases - for the head and the tail
        if (node == self.head):
            self.head = self.head.next
        if (node == self.tail):
            self.tail = self.tail.prev 
        self.removeNodeBindings(node)
        

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value !=value:
            node = node.next
        return node is not None
    
    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None