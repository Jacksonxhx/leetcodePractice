from collections import deque

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if k > n:
            return skills.index(max(skills))
        
        copy = skills
        skills = deque(skills)
        
        tmp = 0
        streak = 0
        cur = skills.popleft()
        
        while streak < k:
            next_ = skills.popleft()
            if cur > next_:
                streak += 1
                skills.append(next_)
            else:
                skills.append(cur)
                cur = next_
                streak = 1
        
        return copy.index(cur)
        