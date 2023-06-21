# def countDistinctWayClimbStairs(nStairs, n=0):

#     if n > nStairs:
#         return 0
    
#     if n == nStairs:
#         return 1
    
#     ans =  countDistinctWayClimbStairs(nStairs, n+1) + countDistinctWayClimbStairs(nStairs, n+2)

#     print(ans)
#     return ans


def countDistinctWayClimbStairs(nStairs):

    if nStairs < 0:
        return 0
    
    if nStairs == 0: 
        return 1
    
    ans =  countDistinctWayClimbStairs(nStairs-1) + countDistinctWayClimbStairs(nStairs-2)

    # print(ans)
    return ans


print(countDistinctWayClimbStairs(5))