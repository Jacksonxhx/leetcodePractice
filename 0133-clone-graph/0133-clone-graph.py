"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        用dfs
        """
        if not node:
            return node
        
        visited = dict()
        
        def dfs(node: 'Node') -> 'Node':
            # 当node已经复制过，直接返回复制之后的
            if node in visited:
                return visited[node]
            
            clone = Node(node.val, [])
            visited[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
        
        return dfs(node)
            