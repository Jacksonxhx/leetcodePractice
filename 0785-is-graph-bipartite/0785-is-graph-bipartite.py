class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        1. 用并查集，分完组后判断每一条边链接的两个node是否在一个set，若在，return False
        
        2. 用DFS，从一个没有被标记的点出发，把跟他相邻的点标记到一个set，自己在另一个set，如果遇到冲突，则返回False
        """
        size = len(graph)
        colors = [0 for _ in range(size)]
        for i in range(len(colors)):
            # 如果遇到了没有链接的node（colors[i] == 0）或者dfs时发现冲突了
            if colors[i] == 0 and not self.dfs(graph, colors, i, 1):
                return False 
        return True
    
    def dfs(self, graph, colors, i, color):
        colors[i] = color
        # 遍历graph[i]的邻边
        for j in graph[i]:
            # 因为邻边的颜色肯定和自己不一样
            if colors[j] == colors[i]:
                return False
            # 如果邻边没有，这次dfs传-color，要和上次不一样
            # 这次从邻边开始找，dfs思想
            if colors[j] == 0 and not self.dfs(graph, colors, j, -color):
                return False
        return True