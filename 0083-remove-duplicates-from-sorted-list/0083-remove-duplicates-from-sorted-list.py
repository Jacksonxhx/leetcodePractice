# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        walk = head
        while walk and walk.next:
            if walk.val == walk.next.val:
                walk.next = walk.next.next
            else:
                walk = walk.next
        
        return head