
##quicksort mai 2 hi step hai.

##--> partition function#
##--> recusrions smbhal lega

def quicksort(arr, s, e):

    if s >=e:
        return
    
    pivot_idx = partition(arr, s, e)

    ##left part sort karo
    quicksort(arr, s, pivot_idx-1)

    ##right part sort karo
    quicksort(arr, pivot_idx+1, e)


def partition(arr, s, e):

    print("For array", arr[s:e+1])

    count_small_nums = 0
    for el in arr[s+1:]:
        # print(el)
        if el < arr[s]:
            # print("yes")
            count_small_nums +=1

    pivot_idx = count_small_nums + s ## yh kar rhe kyunki hamesh s =0 nahi hoga.
    # print("pivot", pivot_idx)
    arr[pivot_idx], arr[s] = arr[s], arr[pivot_idx]

    print(arr)

    i = s
    j = e

    ##thoda complicated hai, par easy hai.
    ## hume pivot element k left mai chote element dalne and right mai bade.
    ## to islie humne upar count krlie chote elements and swap krdia .
    ## or ab i ko tab tak badate jao jab tak pivot index se chota hi hai.
    ## esehi j ko kam krte jao.
    ## dono rukenge means ab yh dono condition disatisfy kr rhe to swap krna padega.
    while (i<pivot_idx and j>pivot_idx):
        
        while(arr[i]< arr[pivot_idx]):
            i +=1
        
        while(arr[j]> arr[pivot_idx]):
            j -=1

        ## firse condition check krlete swap krne se phle.
        if i<pivot_idx and j>pivot_idx:
            arr[i], arr[j] = arr[j] , arr[i]

    print("after", arr)

    return pivot_idx

l1 = [2,5,1,6,9]
quicksort(l1, 0, 4)
print(l1)