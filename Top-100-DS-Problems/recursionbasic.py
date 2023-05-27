def powerOfTwo(n):

    ## base case
    if n==0:
        return 1
    
    smallerProblem = powerOfTwo(n-1)
    biggerProblem = 2*smallerProblem
    

    return biggerProblem

# print(powerOfTwo(1))


def factorial(n):

    if n==0 or n==1:
        return 1
    
    smallerProblem = factorial(n-1)
    biggerProblem = n * smallerProblem

    return biggerProblem

print(factorial(0))


def printNumOpporder(n):

    if n == 0:
        print(0)
        return
    
    print(n)

    printNumOpporder(n-1)

printNumOpporder(4)

def printNum(n):

    if n == 0:
        return 
    
    printNum(n-1)

    print(n)

printNum(4)