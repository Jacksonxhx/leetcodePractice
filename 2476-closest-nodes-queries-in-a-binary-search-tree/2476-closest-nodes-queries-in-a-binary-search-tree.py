# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # infix find the sorted array and then process query
        array = []
        def infix(node):
            if node:
                infix(node.left)
                array.append(node.val)
                infix(node.right)
        infix(root)
        
        n = len(array)
        
        def binary_search(array, target):
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if array[mid] == target:
                    return mid
                elif array[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
            
            
        res = []
        for query in queries:
            index = binary_search(array, query)
            
            if index < n and array[index] == query:
                res.append([array[index], array[index]])
            else:
                smaller = array[index - 1] if index - 1 >= 0 else -1
                larger = array[index] if index < n else -1
                res.append([smaller, larger])
        
        return res
                