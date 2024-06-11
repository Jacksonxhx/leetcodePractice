# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        假设a和b有共同长度k，所以A=m+k，B=n+k。所以A+B = B+A
        '''
        if not headA or not headB:
            return None
        
        pA = headA
        pB = headB
        
        while pA != pB:
            pA = pA.next if pA != None else headB
            pB = pB.next if pB != None else headA
        
        return pA