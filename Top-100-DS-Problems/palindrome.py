## O(n^2): Time | O(n): space
def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return reversedString == string

## O(n): Time | O(n): space
def isPalindrome(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    
    return string == "".join(reversedChars)

## O(n): Time | O(n): space
def isPalindrome(string, i=0):
    j = len(string) -1 - i
    return True if i>= j else string[i] == string[j] and isPalindrome(string, i+1)

## Tail recursive solutiom: not get it.

def isPalindrome(string, i=0):
    j = len(string) -1 - i
    if i>=j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome(string, i+1)

## O(n) time | O(n): space
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) -1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx +=1
        rightIdx -=1
    return True

print(isPalindrome("abcedcba"))
 