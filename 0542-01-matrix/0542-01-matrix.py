from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        BFS每一个点，把所有的0加入queue，遇到1return distance，一直更新。
        这样只需要遍历一遍
        """
        rows, cols = len(mat), len(mat[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        visited = set()
        
        # 统计所有的0的点
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    visited.add((row, col))
        
        # 把0加入queue
        queue = collections.deque(visited)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                nx, ny = dx + i, dy + j
                # 如果找到1
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    # 每个1由最近的i，j再 + 1
                    res[nx][ny] = res[i][j] + 1
                    # 放进queue
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        return res