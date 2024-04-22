# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        通过preorder找root
        通过inorder分割左右子树
        """
        def createTree(preorder: List[int], inorder: List[int], n: int) -> Optional[TreeNode]:
            # base case
            if n == 0:
                return None
            
            # 因为对于每一个子树来说preorder[0] is root，所以从0开始找，通过preorder[0]找inorder哪个是root
            k = 0
            while preorder[0] != inorder[k]:
                k += 1
            
            # 创一个新的node，是每个子树的root
            node = TreeNode(inorder[k]) # root in each subtree
            
            # 对于preorder：k+1指的是preorder左子树的范围，因为k是root，k+1是右子树的开始
            # 对于inorder：是左子树，不包括root的所有左子树node值
            # k：从左到右k个
            node.left = createTree(preorder[1:k+1], inorder[0:k], k)
            
            # 对于preorder：k+1是右子树的开始，
            # 对于inorder：是右子树，不包括root的所有右子树node值
            # n-k-1: 从root+1开始到结尾的数量
            node.right = createTree(preorder[k+1:], inorder[k+1:], n-k-1)
            
            return node
        return createTree(preorder, inorder, len(inorder))
            
            