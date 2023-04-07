def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                swap(j, j+1, array)
    return array
        
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(bubbleSort([-23,100,4,1,8,2,103,9,5,6,3,1,0,23])) 