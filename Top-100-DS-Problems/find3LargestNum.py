## Ex: [141,1,17,-7-17,-27,18,541,8,7,7] should return [18,141,154]

def findThreeLargestNum(array):

    largestNum = [None, None, None] ## contains element in increasing order smallest largest to largest largest

    for num in array:
        ## Updating the num in the largestnum array at index whixh is smaller than the current number.
        updateLargest(largestNum, num)

    return largestNum

def updateLargest(largestNum, num):
    ## This function will put the value at that index if current value in original array is greater than that index
    if largestNum[2] is None or num > largestNum[2]:
        shiftAndUpdate(largestNum, num, 2)
    elif largestNum[1] is None or num > largestNum[1]:
        shiftAndUpdate(largestNum, num, 1)
    elif largestNum[0] is None or num > largestNum[0]:
        shiftAndUpdate(largestNum, num, 0)
    print(largestNum)

## performing the shifting of the index if num is inserted at index 2 then we have to shift value of 2 to 2 and 1 to 0 and at index 2 we will have the number
def shiftAndUpdate(array, num, idx):
    for i in range(0, idx+1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]

print(findThreeLargestNum([141,1,17,-7-17,-27,18,541,8,7,7]))