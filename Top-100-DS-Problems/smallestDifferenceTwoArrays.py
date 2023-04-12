def smallestDiff(array1, array2):

    idx1 = 0
    idx2 = 0
    array1.sort()
    array2.sort()
    mindif = float("inf")
    
    while idx1 < len(array1) and idx2 < len(array2):
        firstNum = array1[idx1]
        secondNum = array1[idx2]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idx1 +=1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idx2 +=1
        else:
            return [firstNum, secondNum]
        if mindif > current:
            mindif = current
            smallestpair = [firstNum, secondNum]
            
    return smallestpair
             