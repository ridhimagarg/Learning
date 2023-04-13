
# O(n) time | O(1) space
def monotonic(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):

        ## if duplicate nums
        if direction == 0:
            direction = array[i] - array[i-1]
            continue
        if breaksDirection(direction, array[i -1], array[i]):
            return False
        
    return True
              
def breaksDirection(direction, previousInt, currentInt):

    difference = currentInt - previousInt
    if direction > 0:
        return difference <0
    return difference > 0

print(monotonic([-1,-5,-10,-11,-13,-16,20]))

## O(n): Time | O(1): space
def monotonic(array):
    isNonDecrreasing = True
    isNonIncreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            isNonDecrreasing = False
        if array[i] > array[i-1]:
            isNonIncreasing = False

    return isNonDecrreasing or isNonIncreasing

print(monotonic([-1,-5,-10,-11,-13,-16,-19]))