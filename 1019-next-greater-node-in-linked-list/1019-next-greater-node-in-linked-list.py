# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        walk = head
        res = []
        
        while walk.next:
            tmp_walk = walk.next
            contain = False
            while tmp_walk:
                if tmp_walk.val > walk.val:
                    res.append(tmp_walk.val)
                    contain = True
                    break
                tmp_walk = tmp_walk.next
            
            if not contain:
                res.append(0)
            walk = walk.next
            
        return res + [0]