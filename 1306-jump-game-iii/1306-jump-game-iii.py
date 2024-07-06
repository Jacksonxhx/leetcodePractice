from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        Bfs找到0，从start开始，return True
        """
        n = len(arr)
        visited = [False] * n
        queue = deque([start])
        
        while queue:
            cur = queue.popleft()
                
            if arr[cur] == 0:
                return True
                
            visited[cur] = True
            
            next_cur = [cur + arr[cur], cur - arr[cur]]
            
            for nc in next_cur:
                if 0 <= nc < n and not visited[nc]:
                    queue.append(nc)
        
        return False
        
        