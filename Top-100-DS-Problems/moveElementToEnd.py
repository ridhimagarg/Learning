
## Time: O(n) | Space: O(1)
def moveElement(array, num):

    leftIdx = 0
    rightIdx = len(array) - 1

    while leftIdx < rightIdx:

        ## [2,1,3,2,4,2,2,2] ## this case needs to be handlled with this while loop.
        while leftIdx < rightIdx and array[rightIdx] == num: ## less than condition because there will be case when we will cross the j and i and then it will swap Ex-: [2,1,2,2,2,3,4,2] run each step and it will fail if we dont put this less than condition.      
            rightIdx -=1
        if array[leftIdx] == num:
            swap(leftIdx, rightIdx, array)
            rightIdx -=1
        leftIdx +=1
             
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]