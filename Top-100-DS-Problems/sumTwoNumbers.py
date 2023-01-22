# Q: Finding the sum of two elements in array which will result the target sum.


## Time Compl -: O(n) and Space Compl -: O(n) because we are storing an extra hash table
## Explanation: Taking a hash table(dictionary) which will contain numbers which we have traversed till now in array.
## Taking the current value from array and subtracting from target sum i.e, y= targetSum - CurrentVal and if y is present in hashtable then will return
## otherwise keep on adding current value to hashtable.

def sumTwoNum(array, targetSum):

    hashnums = {}

    for value in array:
        if targetSum - value in hashnums:
            return [value, targetSum-value]
        else:
            hashnums[value] = True

    return []

## Time Compl -: O(nlogn), Sapxe -: O(1) as no extra space
## Explanation: Sort the array in increasing order which we assumes to be sorted by best sorting algorithm which takes O(nlogn).
## Now using two pointers one on left and one on right, taking sum if sum==tagetsum : return , elif sum < targetsum that means we have to increase the sum so if we 
## move right pointer to left will decrease the sum, hence will move left pointer hence it will increase the sum. elif sum> targetsum, then will move right pointer to left side.

def sumTwoNum(array, targetSum):

    array.sort()
    leftIndx = 0
    rightIndx = len(array) -1 

    while leftIndx < rightIndx:
        sum_ = array[leftIndx] + array[rightIndx]

        if sum_ == targetSum:
            return [array[leftIndx], array[rightIndx]]
        elif sum_ < targetSum:
            leftIndx +=1
        else:
            rightIndx -=1

    return []


print(sumTwoNum([1,10,9,6,-7,2,4], 5))
