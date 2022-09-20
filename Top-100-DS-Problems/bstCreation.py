## Time and Space Complexity

## Average
## time -> o(log(N))
## space -> o(log(N)) ## if uses recursive procedure o(1) -> if uses iterative

## Worst

## time -> o(N)
## space -> o(N) , o(1) -> if uses iterative

from inspect import currentframe


class BST:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None

    ## this is ietrative procedure
    ## Average: O(log(N)) time | O(1) space
    ## Worst: O(N) time | O(1) space
    def insert(self, value):

        currentNode = self

        while True:

            if value < currentNode.value:

                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left

            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right

        return self 

   ## this is ietrative procedure
    ## Average: O(log(N)) time | O(1) space
    ## Worst: O(N) time | O(1) space
    def contains(self, value):

        currentNode = self

        while currentNode is not None:

            if value < currentNode.value:
                currentNode = currentNode.left 
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        
        return False

    def getMinValue(self):
        currentNode = self
        while currentNode is not None:
            currentNode = currentNode.left

        return currentNode.value

    def remove(self, value, parentNode=None):

        currentNode = self

        while currentNode is not None:

            if value < currentNode.value:
                parentNode = currentNode

                currentNode = currentNode.left

            elif value > currentNode.value:

                parentNode = currentNode

                currentNode = currentNode.right
            
            else:
                ## HANDLING CAses where the node to be removed has both the left and right child
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)

                
                ## Handling cases where we have either one child node or None
                ## there could be two cases if node we are deleting is parent node.

                ## if parent node is not there.
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right

                    else:
                        currentNode.value = None

                ## these two cases when parent node is there.
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right

                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right

                

        

    # def printBST(self):

    #     while True:


bst = BST(7)

print(bst.insert(3).right.value)