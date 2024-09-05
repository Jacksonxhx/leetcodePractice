from collections import defaultdict

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 1
        last_day_task = defaultdict(int)
        
        for task in tasks:
            # 需要冷却的情况
            if task in last_day_task and day - last_day_task[task] <= space:
                day = last_day_task[task] + space + 1
            
            # 正常情况
            last_day_task[task] = day
            day += 1
        
        return day - 1