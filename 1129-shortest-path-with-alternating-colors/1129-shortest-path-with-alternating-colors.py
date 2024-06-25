from collections import deque, defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 建图，分别存红色和蓝色
        # 然后BFS每个点存路径，交替从红蓝两张图取
        # 最后判断是否alternative in color
        
        # 用聆接表建图
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        
        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)
        
        # 初始化队列，将从节点 0 出发的红色边和蓝色边分别加入队列
        queue = deque([(0, 0, 'red'), (0, 0, 'blue')])  # (node, step, color)
        distances = [[-1, -1] for _ in range(n)]  # distances[node][0] for red, [1] for blue
        distances[0] = [0, 0]  # 起点的距离为0
        
        while queue:
            node, step, color = queue.popleft()
            next_step = step + 1
            if color == 'red':
                for neighbor in blue_graph[node]:
                    if distances[neighbor][1] == -1:
                        distances[neighbor][1] = next_step
                        queue.append((neighbor, next_step, 'blue'))
            else:
                for neighbor in red_graph[node]:
                    if distances[neighbor][0] == -1:
                        distances[neighbor][0] = next_step
                        queue.append((neighbor, next_step, 'red'))
        
        # 处理结果
        result = []
        for red_distance, blue_distance in distances:
            if red_distance == -1 and blue_distance == -1:
                result.append(-1)
            elif red_distance == -1:
                result.append(blue_distance)
            elif blue_distance == -1:
                result.append(red_distance)
            else:
                result.append(min(red_distance, blue_distance))
        
        return result