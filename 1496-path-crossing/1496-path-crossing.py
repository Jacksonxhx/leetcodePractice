class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # N E S W
        directions = {'N': (1, 0), 'E': (0, 1), 'S': (-1, 0), 'W': (0, -1)}
        walk, visited = (0, 0), set()
        visited.add(walk)
        for ch in path:
            walk = (walk[0] + directions[ch][0], walk[1] + directions[ch][1])
            if walk in visited:
                return True
            visited.add(walk)
        
        return False
        