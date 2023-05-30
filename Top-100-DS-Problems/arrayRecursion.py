def isSortedArray(arr, size):

    ## this is the base case : if initial array is of size 0 or lets say keep on iterating you are left with one element then have to stop
    if size ==0 or size ==1:
        return True
    
    ## if array is not sorted, then current comparision will return False
    elif arr[0] > arr[1]:
        return False
    
    ## this will keep on going untill the array is empty because second condition will stop if array is unsorted.
    else:
        return isSortedArray(arr[1:], size-1)

arr = [1,2,3,4,5,6]
print(isSortedArray(arr, len(arr)))






def LinearSearch(arr, size, key):

    ## yh base case hai
    if size == 0:
        return False
    
    ## kind of one of the stopping criteria or it will start lopping back the recursion.
    elif arr[0] == key:
        return True
    
    else:
        return LinearSearch(arr[1:], size-1, key)
    

arr = [1,2,3,4,5,6]
print(LinearSearch(arr, len(arr), 4))