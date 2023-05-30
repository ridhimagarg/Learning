def powerOfTwo(n):

    ## base case
    if n==0:
        return 1
    
    ## recursion relation
    smallerProblem = powerOfTwo(n-1)
    biggerProblem = 2*smallerProblem

    ## no processing here like printing or something.
    

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

    ## base case
    if n == 0:
        print(0)
        return
    
    ## provcessing
    print(n)

    ## recursion relation
    printNumOpporder(n-1)

print("Printing")
printNumOpporder(4)

def printNum(n):

    if n == 0:
        return 
    
    printNum(n-1)

    print(n)

print("Printing num")
printNum(4)

def reachHome(src, dst):

    if dst == src:
        print(src)
        return
    
    print(src)
    src +=1

    reachHome(src, dst)

print("Ghar phauchna hai")
reachHome(1, 10)