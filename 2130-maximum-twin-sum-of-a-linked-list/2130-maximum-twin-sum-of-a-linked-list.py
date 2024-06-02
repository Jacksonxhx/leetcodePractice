# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        两种方法：
        1. 存array然后双指针更新
        2. 切一半，然后reverse之后加起来
        '''
        # 找到middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        pre, cur = None, slow
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        
        res = 0
        first_half, second_half = head, pre
        while second_half:
            res = max(res, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
            
        return res