"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        用bfs遍历，然后每一层append next指针，每一层的最后一个append null
        需要持续记录每一层最右边一个node
        """
        if not root:
            return None
    
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                
                if i == level_size - 1:
                    node.next = None
                else:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root