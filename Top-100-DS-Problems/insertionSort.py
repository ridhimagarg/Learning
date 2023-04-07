
## Time: O(N^2) | Space: O(1)
def insertionSort(array):

    for i, e in enumerate(array):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                swap(j, j-1, array)

    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(insertionSort([1,8,2,9,5,6,3,1,7])) 