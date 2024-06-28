from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Initialize color array with -1 (uncolored)
        color = [-1] * len(graph)
        
        # Iterate through each node in the graph
        for i in range(len(graph)):
            # If the node is not colored, perform BFS
            if color[i] == -1:
                # Start BFS from the node
                queue = deque([i])
                # Color the starting node with color 0
                color[i] = 0
                
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            # Color the neighbor with opposite color
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            # If neighbor has the same color, it's not bipartite
                            return False
        return True
