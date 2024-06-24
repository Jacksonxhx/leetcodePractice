class Solution:
    # backtrack做dfs
    def dfs(self, graph, start, target, path, ans):
        # 当找到target后，append
        if start == target:
            ans.append(path[:])
            return
        
        # 依次做bracktrack
        for end in graph[start]:
            path.append(end)
            self.dfs(graph, end, target, path, ans)
            path.remove(end)
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        从第 0 个节点开始进行深度优先搜索遍历。在遍历的同时，通过回溯来寻找所有路径
        """
        path = [0]
        ans = []
        self.dfs(graph, 0, len(graph) - 1, path, ans)
        return ans
    