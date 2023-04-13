
## Iterative solution
## Tine: O(n) | Space: O(n) (results array) other no extra soace to solve the solution.
def spiralTraverse(array):

    result = []
    startRow, endRow = 0, len(array) -1
    startCol, endCol = 0, len(array[0]) -1

    while startRow < endRow and startCol < endCol:

        for col in range(startCol, endCol +1):
            result.append(array[startRow][col])
        
        for row in range(startRow +1,endRow+1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])

        for row in reversed(range(startRow+1, endRow)):
            result.append(array[row][startCol])

        startRow +=1
        endRow -=1
        startCol +=1
        endRow -=1

    return result 


## O(n): Time , O(n): space , result ki space hai, recusrion space zada nahi lega to count nahi kr rhe, in this case.
def spiralTraverse(array):
    result = []
    spiralFill(array, 0, len(array)-1, 0, len(array[0])-1, result)
    return result

def spiralFill(array, startRow, endRow, startCol, endCol, result):

    if startRow > endRow and startCol > endCol:
        return
    
    for col in range(startCol, endCol +1):
            result.append(array[startRow][col])
        
    for row in range(startRow +1,endRow+1):
        result.append(array[row][endCol])

    for col in reversed(range(startCol, endCol)):
        result.append(array[endRow][col])

    for row in reversed(range(startRow+1, endRow)):
        result.append(array[row][startCol])
    
    spiralFill(array, startRow+1, endRow-1, startCol+1, endCol-1, result)