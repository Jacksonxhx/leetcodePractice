from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # 建立站点和bus点映射
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        print(stop_to_routes)
        
        # bfs
        queue = deque([(source, 0)])
        visited_stops = set([source])
        visited_routes = set()
        
        while queue:
            stop, bus_count = queue.popleft()
            
            for route_idx in stop_to_routes[stop]:
                if route_idx in visited_routes:
                    continue
                    
                for next_stop in routes[route_idx]:
                    if next_stop == target:
                        return bus_count + 1
                    
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, bus_count + 1))
                
                visited_routes.add(route_idx)
        
        return -1
        