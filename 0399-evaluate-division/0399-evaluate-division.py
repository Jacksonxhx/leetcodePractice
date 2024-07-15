from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        a/b = 2其实就是 a -> b cost 2, b -> a cost 1/2
        用equations建图，然后用query找
        """
        
        graph = {}
        
        # 建图
        def build_graph(equations, values):
            def add_edge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]
            
            for vertices, value in zip(equations, values):
                f, t = vertices
                # 正反都要append
                add_edge(f, t, value)
                # 反过来就是1/value
                add_edge(t, f, 1/value)
    
        # 找query
        def find_path(query):
            b, e = query
            
            if b not in graph or e not in graph:
                return -1.0
            
            queue = collections.deque([(b, 1.0)])
            visited = set()
            
            # BFS
            while queue:
                front, cur_product = queue.popleft()
                
                # 当遍历到query下一个时
                if front == e:
                    return cur_product
                
                visited.add(front)
                
                # bfs遍历邻接点
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        queue.append((neighbor, cur_product*value))
            
            return -1.0
        
        build_graph(equations, values)
        return [find_path(query) for query in queries]
            