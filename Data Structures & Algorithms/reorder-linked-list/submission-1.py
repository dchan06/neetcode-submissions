# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # using fast and slow pointers, find the halfway point of the list
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        first_half, second_half = head, slow

        # reverse the second half of the list
        temp = second_half.next
        prev = second_half.next = None 
        second_half = temp
        while second_half != None: 
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp
        second_half = prev
        
        # merge
        while first_half != None and second_half != None: 
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half 
            second_half.next = first_half = temp1
            second_half = temp2
        head = first_half
            
        


