# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        用recursion
        '''
        if not head or not head.next:
            return head
        
        dummy = head.val
        head.val = head.next.val
        head.next.val = dummy
        
        head.next.next = self.swapPairs(head.next.next)
        
        return head