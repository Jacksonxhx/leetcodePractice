import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        返回一个拓扑序
        '''
        # 构建一个图
        graph = dict()
        for i in range(numCourses):
            graph[i] = []
        
        # 找到pre对应哪些边
        for v, u in prerequisites:
            graph[u].append(v)
            
        return self.topoSort(numCourses, graph)
            
    
    def topoSort(self, numCourses, graph) -> List[int]:
        res = []
        # 构建一个入度哈希表
        indegrees = {u: 0 for u in graph}
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1
        
        # 用一个队列维护入度为0的node
        S = collections.deque([u for u in graph if indegrees[u] == 0])
        
        while S:
            u = S.pop()
            res.append(u)
            numCourses -= 1
            # 移除被u链接的入度
            for v in graph[u]:
                indegrees[v] -= 1
                # 重新appendv到S中
                if indegrees[v] == 0:
                    S.append(v)
                    
        if numCourses == 0:
            return res
        return []