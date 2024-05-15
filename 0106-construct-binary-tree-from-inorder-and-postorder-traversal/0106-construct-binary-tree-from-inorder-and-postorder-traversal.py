# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        根据post或者preorder找根节点，然后根据inorder把preorder找到的节点分为左右子树
        然后递归，重新继续对左右子树分别分割
        分割到最后就会到base case，就是children，然后就会创建node
        然后会递归上去
        
        本质就是不停的左右分割
        '''
        def create_tree(inorder, postorder, n):
            if n == 0:
                return None
            
            # 通过postorder找到根节点在inorder的位置
            k = 0
            while postorder[n - 1] != inorder[k]:
                k += 1
            
            node = TreeNode(inorder[k])
            
            node.right = create_tree(inorder[k+1: n], postorder[k: n-1], n-k-1)
            node.left = create_tree(inorder[0: k], postorder[0: k], k)
            
            return node
        
        return create_tree(inorder, postorder, len(inorder))
            