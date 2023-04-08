def selectionSort(array):
    for i in range(len(array)):
        index = i
        for j in range(i+1,len(array)):
            if array[j] < array[index]:
                index = j
        swap(index, i, array)
    return array


def swap(i, j, array): 
    array[i], array[j] = array[j], array[i] 


print(selectionSort([-23,100,4,1,8,2,103,9,5,6,3,1,0,23])) 