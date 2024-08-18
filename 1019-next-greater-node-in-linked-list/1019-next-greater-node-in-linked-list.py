# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # 用单调栈去一直更新
        res = []
        monostack = []
        def f(node, i):
            if node is None:
                nonlocal res
                # 从后往前，走到底开始initialization
                res = [0] * i # i是链表长度
                return
            # 递归，相当于从后往左查
            f(node.next, i + 1)
            # 当栈顶的元素小于当前，把该元素pop掉
            while monostack and monostack[-1] <= node.val:
                monostack.pop()
            if monostack:
                # 每个栈顶剩下的就是比当前大的
                res[i] = monostack[-1] 
            monostack.append(node.val)
        f(head, 0)
        return res