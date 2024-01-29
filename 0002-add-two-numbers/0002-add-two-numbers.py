# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        time = 1
        val = 0
        l1_val, l2_val = 0, 0

        # get val
        while l1 or l2:
            
            l1_val = l1.val * time if l1 else 0
            l2_val = l2.val * time if l2 else 0
            
            val += l1_val
            val += l2_val
            
            time *= 10
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        digits = [int(digit) for digit in str(val)]
        
        dummy = ListNode()
        current = dummy
        
        for i in range(len(digits) - 1, -1, -1):
            current.val = digits[i]
            if i - 1 < 0:
                current.next = None
            else:
                current.next = ListNode()
                current = current.next
            
        return dummy
        