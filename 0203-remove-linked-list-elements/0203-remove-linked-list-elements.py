# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode()
        dummy.next = head
        walk = dummy
        
        while walk.next:
            if walk.next.val == val:
                walk.next = walk.next.next
            else:
                walk = walk.next
        
        return dummy.next