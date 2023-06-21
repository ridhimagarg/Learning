def reverseString(i, j, string):

    string_list = list(string)
    if i>j:
        return str(string_list)
    print(i)
    print(j)
    temp = string_list[i]
    string_list[i] = string_list[j]
    string_list[j] = temp

    i +=1
    j -=1
    reverseString(i, j, string)

string = "abcdef"
print(len(string))
print(reverseString(0, len(string)-1, string))

# palindrome string 



# power

def power(a, pow):

    if pow == 0:
        return 1
    
    if pow == 1:
        return a
    
    ans = power(a, pow/2) 

    if pow % 2 == 0:
        return ans * ans
    else:
        return a * ans * ans
    

# print(power(2, 5)) # not working for odd power


## bubble sort

def bubblesort(arr, n):

    if (n==0 or n ==1):
        print("arr", arr)
        print("here")
        return arr
    
    ## one iteration of sorting
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        print(arr)

    ## baaki recursion sambhal lega
    bubblesort(arr, n-1)

print(bubblesort([1,8,3,4,5], 5))




