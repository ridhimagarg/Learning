
# Time : O(n) | Space: O(1)
def reverseLinkedList(head):
    p1 = None
    p2 = head

    while p2 is not None:
        p3 = p2.next ## if we move this line outside the loop. then at line 11 p2 as the tail of LL, then p3 as null
        p2.next = p1
        p1 = p2 
        p2 = p3 
        # p3 = p3.next ## then this line p3 will give error (comment read at line 8)
    
    return p1
    

