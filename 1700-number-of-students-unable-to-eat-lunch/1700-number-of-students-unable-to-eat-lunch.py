from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        stack = deque(sandwiches)
        
        size = len(students)
        tmp = 0
        
        while queue:
            if tmp > size:
                break
            if queue[0] == stack[0]:
                queue.popleft()
                stack.popleft()
                tmp = 0
            else:
                queue.append(queue.popleft())
                tmp += 1
        
        return len(queue) 