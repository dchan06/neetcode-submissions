# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr != None: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        start = curr = prev
        nxt = prev.next
        count = 1
        while curr != None:
            if count >= (n - 1): 
                if nxt == None:
                    return head.next
                elif n == 1:
                    start = nxt
                else:
                    temp = nxt.next
                    curr.next = temp
                break
            curr = curr.next
            nxt = curr.next
            count += 1
        prev = None
        while start != None: 
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        return prev