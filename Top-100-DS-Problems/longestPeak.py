
## We are going to divide this prolem into two -: finding peaks, and the out of thosse we find the longest one. 
def longestPeak(array):

    indices = findPeaks(array)

    # lenPeak = []
    lenPeak = float("-inf")
    longestPeakIndex = -1
    for index in indices:

        leftIdx = 1
        rightIdx = 1
        i = index 
        while array[i-2] < array[i-1] and i >= 2:
            leftIdx +=1 
            i -=1

        j = index
        while j < (len(array)-2) and array[j+2] < array[j+1]:
            rightIdx +=1
            j +=1

        print(leftIdx)
        print(rightIdx)
        if  (rightIdx+leftIdx+1) > lenPeak:
            lenPeak = rightIdx+leftIdx+1
            longestPeakIndex = index

        
    return lenPeak, longestPeakIndex


def findPeaks(array):

    indices = []
    for i in range(1, len(array)-1):
        if array[i-1] < array[i] and array[i] > array[i+1]:
            indices.append(i)
    return indices

print(longestPeak([1,2,3,4,3,2,1,0,-1,-2,10,6,5,-1,-3,-4,-5]))