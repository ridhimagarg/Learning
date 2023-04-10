
## Worst: Time: O(N^2), Best: Time: O(nlog(N)), Space: O(log(N))
def quickSort(array):
      quickSortHelper(array, 0, len(array)-1)
      return array

def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx ## This is how we are choosing pivot, but there are other ways to do so.
    leftIdx = startIdx + 1
    rightIdx = endIdx

    ## This while loop contains the main logic of the quicksort
    while leftIdx <= rightIdx:
        ## We will only swap the elements if leftidx is greater than pivot and rightidx is less than pivot (Since we want that leftsubarray to pivot should be samller and rightsubarray should be larger)
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                swap(leftIdx, rightIdx, array)
        ## If leftidx is smaller which is a right condition then will move pointer of leftidx
        if array[leftIdx] <= array[pivotIdx]:
                leftIdx +=1
        ## Same for the rightidx, If rightidx is greater which is a right condition then will move pointer of rightidx
        if array[rightIdx] >=  array[pivotIdx]:
                rightIdx -=1
    ## once we are done with one iteration of quicksort of that suba array we will swap the rightidex with the pivotindex.
    swap(rightIdx, pivotIdx, array)

    ## Now we will perform quicksort on the subarrays.
    ## Condition is to perform the quicksort on the smallest subarray.
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)

    ## if leftsubarray is smaller, will sort leftsubarray first.
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx-1)
        quickSortHelper(array, rightIdx+1, endIdx)
    ## if rightsubarray is smaller.
    else:
        quickSortHelper(array, rightIdx+1, endIdx)
        quickSortHelper(array, startIdx, rightIdx-1)

    
def swap(i, j, array): 
    array[i], array[j] = array[j], array[i] 

print(quickSort([-23,100,4,1,8,2,103,9,5,6,3,1,0,23])) 