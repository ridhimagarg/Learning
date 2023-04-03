#Ex: [5,2, [7,-1], 3, [6, [-13,8], 4] ] Returns: 12
# Solution 5 +2 + (Noe recursive caLL for [7,-1] -: (7+(-1))*2 = 12) +12 + 3 + (Now again recursive, 6 + again recursive(-13+8)*3= -15 + 4= -5*2= 10)+10

## Solving it with recusrion
def productSum(array, multiplier=1):

    sum = 0

    for element in array:
        if isinstance(element, list):
            sum  += productSum(element, multiplier+1)
        else:
            sum += element
        
    return sum * multiplier

print(productSum( [5,2, [7,-1], 3, [6, [-13,8], 4] ]))

