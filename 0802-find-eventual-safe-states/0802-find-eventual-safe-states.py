import collections

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        按照拓扑序排好之后，不在环里的点就是safe，因为最终这些点都会到一个出度为0的node
        按照逆序建图，这样出度为0的终点就变为了入度为0的点
        也可以不逆序，直接处理，拓扑排序后把环node全部去掉
        """
        # 首先构建图
        graph_dict = {u: [] for u in range(len(graph))}
        
        # 逆序建图
        for u in range(len(graph)):
            for v in graph[u]:
                graph_dict[v].append(u)

        return self.topologicalSortingKahn(graph_dict)
    
    def topologicalSortingKahn(self, graph_dict):
        # indegrees 用于记录所有节点入度
        indegrees = {u: 0 for u in graph_dict}   
        for u in graph_dict:
            for v in graph_dict[u]:
                indegrees[v] += 1 
        
        # 将入度为 0 的顶点存入集合 S 中
        S = collections.deque([u for u in indegrees if indegrees[u] == 0])
        
        # 当S有
        while S:
            # 获取出度为0的node
            u = S.pop()
            # 因为逆建图，这里找到的是什么node到了u
            for v in graph_dict[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    S.append(v)
        
        res = []
        for u in indegrees:
            # 统计没有环的点，如果不在环，最后的逆序建图后，排序后入度一定为0
            if indegrees[u] == 0:
                res.append(u)
        
        return res
        
        