class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        DFS搜scc，就是求有多少个scc
        我们可以对每个未访问过的节点进行DFS，标记所有与之直接或间接相连的节点为访问过
        '''
        def dfs(i: int):
            # 对i中的每个j遍历，如果是1，则是i这个node的scc中的一个，加入visited
            # 然后沿着这个j做一样的事儿
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
        
        # define 长度，联通块array，scc数量
        n = len(isConnected)
        visited = [False] * n
        scc = 0
        
        # 遍历所有的节点，
        for i in range(n):
            # 如果没有走到，就是找到了新的scc
            # 每次dfs之后，都会把当前所在的node更新
            if not visited[i]:
                dfs(i)
                scc += 1
                
        return scc