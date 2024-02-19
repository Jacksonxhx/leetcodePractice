# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the element just before the start of the reversal segment
        for _ in range(left - 1):
            prev = prev.next
        
        # Start the reversal process
        reverse = None
        current = prev.next
        for _ in range(right - left + 1):
            next_temp = current.next
            current.next = reverse
            reverse = current
            current = next_temp
        
        # Connect the reversed segment back to the list
        prev.next.next = current
        prev.next = reverse
        
        return dummy.next