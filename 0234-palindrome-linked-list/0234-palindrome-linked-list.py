# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        O(n), O(1)做法，reverse前一半，然后comp后一半
        '''
        rev = None
        slow = fast = head
        while fast and fast.next:
            # 更新fast
            fast = fast.next.next
            
            # 更新slow，且找到中点
            # 逻辑：把下一个指向上一个，且一直更新slow
            rev, rev.next, slow = slow, rev, slow.next
            
        # 如果是奇数，slow往前一个    
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        
        return not rev