
## Time: O(N^2) | Space: O(1)
## Best case O(N): if we dint perform any swap in the first time then we can check if didnt perform then array is already sorted (another implementation)
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                swap(j, j+1, array)
    return array
        
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(array) -1- counter): 
            if array[i] > array[i+1]:
                swap(i, i +1, array)
                isSorted = False
        counter +=1
    return array
         

print(bubbleSort([-23,100,4,1,8,2,103,9,5,6,3,1,0,23])) 