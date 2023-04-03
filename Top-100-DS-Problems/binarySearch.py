## If some problem is having sorted arry then probably binary serach is one of the technique to apply. 


## This is a recursive approach.
## Time: O(log(N)) | Space: O(log(N)), sopace takes up by stacking the calls.
def binarySearch(array, target):
     return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
     
    if left > right:
        print("Left index", left)
        print("Right index", right)
        return -1
    middle = (left +right)//2
    potentialMatch = array[middle]

    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        right = middle -1
        return binarySearchHelper(array, target, left, right)
    else:
        left = middle + 1
        return binarySearchHelper(array, target, left, right)
    
print(binarySearch([0,1,21,33,45,45,47,61,71,72,73], 33))
print(binarySearch([0,1,21,33,45,45,47,61,71,72,73], 74))
print(binarySearch([0,1,21,33,45,45,47,61,71,72,73], -4))


## This is an iterative approach
## Time: O(log(N)) | Space: O(1)
def binarySearch(array, target, left, right):

    left = 0 
    right = len(array) -1
    while left <= right:
        middle = (left + right)//2
        potentialMatch = array[middle]

        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle -1
        else:
            left =  middle + 1
    return -1

print(binarySearch([0,1,21,33,45,45,47,61,71,72,73], 33, 0, 0))
print(binarySearch([0,1,21,33,45,45,47,61,71,72,73], 74, 0, 0))
print(binarySearch([0,1,21,33,45,45,47,61,71,72,73], -4, 0, 0))
