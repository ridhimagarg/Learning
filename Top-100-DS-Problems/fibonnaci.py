## Time: O(2^n) | Space: O(n) - explaination ipad
## Recursive solution but bad time complex.
def getNthFib(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)
    
print(getNthFib(4))


##=============================================
## recursive solution with good time but still taking space.
## Time: O(n) | Space: O(n)
def getNthFib(n, memoize= {1: 0, 2: 1}):

    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        return memoize[n]
    
print(getNthFib(4))


##=======================================================
## Iterative solution. goof time and space.
## Time O(n) | Space O(1)
def getNthFib(n):

    lastTwo = [0,1]
    counter = 3
    while counter <=n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter +=1
    return lastTwo[1] if n>1 else lastTwo[0]

print(getNthFib(4))

