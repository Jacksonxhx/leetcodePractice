from collections import defaultdict, deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        # 用bfs找最短路
        res = [0] * n
        # 先建图，双向建图
        adjacency_list = defaultdict(list)
        for i in range(1, n):
            adjacency_list[i].append(i + 1)
            adjacency_list[i + 1].append(i)
        
        # 加入多的那条边
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)
        
        def bfs(i):
            queue, visited = deque(), set()
            # 第几条街，走过多少条路
            queue.append((i, 0))
            visited.add(i)
        
            while queue:
                i, dist = queue.popleft()
                
                # 更新res
                if dist > 0:
                    res[dist - 1] += 1
                    
                for neighor in adjacency_list[i]:
                    if neighor not in visited:
                        visited.add(neighor)
                        queue.append((neighor, dist + 1))
        
        # 依次遍历各个房子
        for i in range(1, n + 1):
            bfs(i)
        
        return res