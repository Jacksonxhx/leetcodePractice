# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        def in_order(node):
            if node:
                in_order(node.left)
                self.res.append(node.val)
                in_order(node.right)
        in_order(root)
        self.index = 0

    def next(self) -> int:
        res = self.res[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        if self.index >= len(self.res):
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()