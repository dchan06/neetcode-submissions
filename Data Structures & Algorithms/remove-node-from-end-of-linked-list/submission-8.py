# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        target = forward = head
        count = 0
        while count < n: 
            forward = forward.next
            count += 1
        if forward == None: 
            return head.next
        while forward != None: 
            if forward.next == None: 
                target.next = target.next.next
            target = target.next
            forward = forward.next

        return head
