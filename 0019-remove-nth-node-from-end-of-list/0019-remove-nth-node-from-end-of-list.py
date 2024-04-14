# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        
        walk = head
        while walk != None:
            size += 1
            walk = walk.next
        
        index = size - n - 1
        if index < 0:
            head = head.next
            return head
        
        walk = head
        while index != 0:
            walk = walk.next
            index -= 1
        
        walk.next = walk.next.next
        
        return head
        