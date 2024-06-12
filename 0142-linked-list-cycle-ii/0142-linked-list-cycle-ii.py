# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1. DFS找back edge
        2. Floyd判圈法，快慢指针追，如果追到了则有环，若快指针指到了None则无环
            从快慢相遇的点到环起始点c，a=c+(n−1)(b+c)
        '''
        slow = fast = head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        
        ans = head
        # 让ans和slow一起动
        while ans != slow:
            ans, slow = ans.next, slow.next
        
        return ans