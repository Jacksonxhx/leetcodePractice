# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tmp_value = [0] * (right - left + 1)
        
        walk = head
        for i in range(left - 1):
            walk = walk.next
        
        for i in range(right - left + 1):
            tmp_value[i] = walk.val
            walk = walk.next
        
        res = head
        for i in range(left - 1):
            res = res.next
        
        for i in range(right - left + 1):
            res.val = tmp_value[-1-i]
            res = res.next
        
        return head