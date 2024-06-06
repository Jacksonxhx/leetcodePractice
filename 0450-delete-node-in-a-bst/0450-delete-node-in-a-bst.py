# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
        递归查找，然后做删除，主要考察BST的删除
        '''
        if not root:
            return root
        
        # 删除BST中的node
        if root.val == key:
            # 当没有左子树时
            if not root.left:
                return root.right
            # 当没有右子树时
            elif not root.right:
                return root.left
            # 剩下的情况:
            # 则将左子树转移到右子树最左侧的叶子节点位置上，然后右子树代替当前节点位置。返回右子树。
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                curr.left = root.left
                return root.right
            
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            root.right = self.deleteNode(root.right, key)
            return root