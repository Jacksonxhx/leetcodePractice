from collections import deque, defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        hasht = defaultdict(list)
        for u, v in adjacentPairs:
            hasht[u].append(v)
            hasht[v].append(u)
        
        start = 0
        for key, value in hasht.items():
            if len(value) == 1:
                start = key
                break
        
        visited = set()
        queue = deque([start])
        nums = []
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                nums.append(node)
                for neighbor in hasht[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return nums