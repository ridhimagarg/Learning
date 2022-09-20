# Q: Validate if this subsequence belongs to sequence
# Ex: [-1,6,1,0] is a validated subsequence of [10,9,-1,8,6,80,1,0]
# Ex: [-1,6,1,0] is not a validated subsequence of [10,9,-1,8,6,80,0,1]


## Time Compl -: O(n)
## Iterating over an array

def validateSubSeq(array, sequence):

    if sequence == [] or len(sequence)> len(array):
        return False

    subIndx = 0

    for value in array:
        if value == sequence[subIndx]:
            subIndx += 1
        if subIndx == len(sequence):
            return True

    return False


print(validateSubSeq([10,9,-1,8,6,80,0,1], [10,9,-100,10,10,10,10,10,10,10,78]))