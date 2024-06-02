# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        用两个指针pre cur，pre指向cur前一个，但每次把cur指向pre
        '''
        pre = None
        cur = head
        
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        
        return pre