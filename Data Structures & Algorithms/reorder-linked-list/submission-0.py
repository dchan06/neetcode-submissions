# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        nxt = ptr = head
        while ptr.next != None:
            if ptr.next.next == None: 
                nxt = ptr
            ptr = ptr.next
            count += 1
        n = count // 2
        while n > 0: 
            if ptr.next == None:
                # move the nodes
                temp = head.next
                head.next = ptr
                ptr.next = temp
                nxt.next = None
                
                # reset the pointers
                head = temp
                nxt = ptr = head.next
                n -= 1
            else:
                if nxt.next.next == None: 
                    ptr = nxt.next
                else: 
                    nxt = nxt.next


