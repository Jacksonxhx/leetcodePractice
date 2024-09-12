# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # 如果当前节点匹配，则递归继续检查左子树和右子树，直到链表全部匹配
        def dfs(head, root):
            if not head: return True
            if not root: return False
            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        
        # 处理特殊情况
        if not head: return True
        if not root: return False
        
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)