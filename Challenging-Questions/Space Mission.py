
# coding: utf-8



## Importing permutations module

from itertools import permutations


# ### Creating usable functions in order to use in our main function



## Usable functions for count function

"""It is calculating the permutations with the first week and all permutations possible in that range(N) so as to get
only those elements which are matching our criteris of distance<d """

def perm_with_first(N,d,first,original):
    
    
    ## Storing the permutations which are matching the criteria
    sel_perm_f = []
    
    ## Iterating to the all the permutations
    for e in original:
        ##Iterating to each element in every permutations
        for i in e:
            ## Conditional check if distance is less than d for all elements in each permutation only then, will add 
            ## that permutation into the final list
            if ((N+ (e.index(i)))- (first.index(i))) < d:
                break 
            elif e.index(i) == (N-1):
                 sel_perm_f.append(e)
    return sel_perm_f


"""It is calculating the permutations with the last week and all permutations possible in that range(N)"""

def perm_with_last(N,d,original,last):   
    
    ## Storing the permutations which are matching the criteria
    sel_perm_l = []
    
    ## Iterating to the all the permutations
    for e in original:
        for i in e:
            ## Conditional check if distance is less than d for all elements in each permutation only then, will add 
            ## that permutation into the final list
            if abs(((e.index(i))- (N + last.index(i)))) < d:
                break 
            elif e.index(i) == (N-1):
                #print(e)
                sel_perm_l.append(e)
    return sel_perm_l
 

""" It is to get the pairs which are satisfying the criteria of distance between elements(shirts) for newly
generated permutations. """   

 
def get_pairs(N,d,sel_perm_f, sel_perm_l):
    
    ## Storing pairs which are actually meeting the criteria of distance.
    
    pairs = []
    
    ## Iterating over selected permutations from first week and last week in order to get pairs which are satisfying their
    ## distance criteria between same shirts.
    
    for e in sel_perm_f:
        for f in sel_perm_l:
            for i in e:
                if abs(((e.index(i))- (N + f.index(i)))) < d:
                    break 
                elif e.index(i) == (N-1):
                    #print(e)
                    pairs.append([e,f])
    return pairs            


## Calculating the intersection of list
def intersection_list(a,b):
    return list([x for x in a if x in b])



""" Calculating if first and last week are meeting the criteria of distance then no need to move forward."""

def dist(N,d,fir,las):
    for i in fir:
            if abs(((fir.index(i))- (N + las.index(i)))) < d:
                return False
            elif fir.index(i) == (N-1):
                return True





# ### Creating a count(main) function




"""defining the count function, with given first week,last week and the d value. 
    There are certain checks like for first week == last week then return 1"""

def count(first_week,last_week,d):
    
    ## Retrieving the value of N from length of first week or last week
    N = len(first_week)
    
    ## Storing the weeks with shirts order
    weeks = []
    
    ## Creating the permutation in the range of N -> To use in upcoming cases.
    
    l = [i for i in range(1,(N+1))]
    orig_perm = permutations(l)
    ## Storing it as a list instead of generator as it will become empty after accessing the values.
    
    orig_perm = list(orig_perm)
    
    
    ## Appending first week and last week into the weeks list
    weeks.append(first_week)
    weeks.append(last_week)
    
    
    ## Checking if first week and last week are same.
    if first_week == last_week:
        print("First week and Last week are same.")
        print(weeks)
        return 1
    

    
    else:
        
        
        ## Checking if first week and last week itself are sufficient to make a mission complete then ddon't proceed. Return 2.
        ## Otherwise proceed.
        if (dist(N,d, first_week,last_week) != True):
        
            ## Caclulating the permutations with first week satisfying the criteria.
            sel_perm_f = perm_with_first(N, d, first_week , orig_perm)
            
            ## Caclulating the permutations with last week satisfying the criteria.
            sel_perm_l = perm_with_last(N, d, orig_perm, last_week)
            
            ## IF comman values occur in both permutation generated using first week and last week then just add one more week 
            ## and return the length of the weeks.
            
            if intersection_list(sel_perm_f,sel_perm_l) != []:
                #print(intersection_list(sel_perm_f,sel_perm_l))
                weeks.insert((len(weeks)-1),list(intersection_list(sel_perm_f,sel_perm_l)[0]))
                print("One possible combination is: \n")
                print(weeks)
                return len(weeks)
            
            ## If no common then will first find pairs.
            else: 
                ## finding pairs
                pairs = get_pairs(N, d, sel_perm_f, sel_perm_l)
                
                ## if pairs are not empty then simply returns the length because we got pairs of weeks which are satisfying
                ## our critera of distsnce.
                
                if pairs != []:
                    weeks.insert((len(weeks)-1),list(pairs[0][0]))
                    weeks.insert((len(weeks)-1),list(pairs[0][1]))
                    print("One possible combination is: \n")
                    print(weeks)
                    return len(weeks)
                
                ## For this case, functiom is not able to handle.
                else:
                    print("Not able to handle this case")
                    return 0
                
        ## Return 2 if first week and last week are susficient to complete the mission itself.
        else:
            print("First week and last week are sufficient to complete the mission")
            print(weeks)
            return 2
            
            
    


# ### Executing the given examples 



print(count([1,2,3,4],[4,3,2,1],3))




print(count([1,2,3,4],[2,1,3,4],3))




print(count([8,5,4,1,7,6,3,2],[2,4,6,8,1,3,5,7],3))




print(count([1,2,3,4],[1,2,3,4],2))

