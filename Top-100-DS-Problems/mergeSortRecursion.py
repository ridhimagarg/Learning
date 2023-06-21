def merge(arr, s, e):
    
    mid = int((s+e)/2)

    len1 = mid - s + 1
    len2 = e - mid
     
    first = [0] * len1
    second = [0] * len2

    ## copy values
    k = s
    for i in range(len1):
        first[i] = arr[k]
        k +=1

    k = mid + 1
    for i in range(len2):
        second[i] = arr[k]
        k +=1

    ## merge 2 sorted arrays
    index1 = 0
    index2 = 0
    mainArrayIndex = s

    while(index1 < len1 and index2 < len2):
        if (first[index1] < second[index2]):
            arr[mainArrayIndex] = first[index1]
            index1 +=1

        else:
            arr[mainArrayIndex] = second[index2]
            index2 +=1
        
        mainArrayIndex +=1

    while (index1 < len1):
        arr[mainArrayIndex] = first[index1]
        index1 +=1
        mainArrayIndex += 1

    while (index2 < len2):
        arr[mainArrayIndex] = second[index2]
        index2 +=1
        mainArrayIndex += 1
    
    # print(arr)





    



def merge_sort(arr, s, e):

    if s >= e:
        return
    
    mid = int((s+e)/2)
    print(mid)

    merge_sort(arr, s, mid)

    merge_sort(arr, mid+1, e)

    merge(arr, s, e)


l1 = [2,5,1,6,9]
merge_sort(l1, 0, 4)
print(l1)

## Do homework