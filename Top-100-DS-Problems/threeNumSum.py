
## O(n^2): time as two loops and nlogn for sorting but n^2 is bigger | O(n): space : storing the triplets
def threeNumSum(array, targetSum):
    array.sort()

    triplets = []
    for i in range(len(array) -2):
        left = i +1
        right = len(array) -1
        while left < right: ## not putting = here because in the even/odd case we dont want overlap.
            currentSum = array[i] +  [left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                ## we are not handling the duplicates over here. lets say  2 is repeated two times then we have to handle those cases..
                left +=1
                right -=1   
            elif currentSum < targetSum:
                left +=1
            elif currentSum > targetSum:
                right -=1
    return triplets


print(threeNumSum([12,3,1,2,-6,5,-8,6], 0))
            

