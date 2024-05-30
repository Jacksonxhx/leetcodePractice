# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        walk = head
        n = 0
        while walk:
            walk = walk.next
            n += 1
        
        middle = n // 2
        tmp = head
        
        while middle > 1:
            tmp = tmp.next
            middle -= 1
        
        tmp.next = tmp.next.next
        
        return head