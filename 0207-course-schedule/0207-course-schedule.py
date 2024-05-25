import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        找是否有环，看是否能走拓扑序，能找到就可以，找不到证明有环则不行
        用khan's algo做，找入度为0的点，加入stack，把用这个点作为入度的点，入度--
        需要整理khan's algo的模版代码
        '''
        # 用dict存所有的点的路径
        graph = dict()
        for i in range(numCourses):
            graph[i] = []
            
        # 统计哪节requisite下有哪些课
        for v, u in prerequisites:
            graph[u].append(v)
        
        return self.topoSort(numCourses, graph)
    
    def topoSort(self, numCourses, graph):
        # 初始化每个节点的入度为0
        indegrees: dict = {u: 0 for u in graph}
        
        # 计算每个点的入度
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1
                
        # 用队列S去获取所有入度为0的点
        S = collections.deque([u for u in indegrees if indegrees[u] == 0])
        
        # 利用队列做topo sort
        while S:
            # 取出改节点
            u = S.pop()
            numCourses -= 1
            for v in graph[u]:
                # 因为u连到v，所以u被拿走后，v入度--
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    S.append(v)
        
        # 如果所有课都被上了
        if numCourses == 0:
            return True
        return False
        
        