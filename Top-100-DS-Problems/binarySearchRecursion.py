def binarySearch(arr, start, end, key):

    mid = int(start + (end - start)/2)

    if start>end:
        return False
    
    elif arr[mid] == key:
        return True

    elif arr[mid]>key:
        return binarySearch(arr, start, end-1, key)

    else:
        return binarySearch(arr, start+1, end, key)
    
arr = [0,1,2,3,5,11,90]
print(binarySearch(arr, 0, len(arr), 90))
