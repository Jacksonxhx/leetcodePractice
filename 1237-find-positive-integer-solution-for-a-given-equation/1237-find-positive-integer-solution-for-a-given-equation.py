"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        """
        1 <= x, y <= 1000
        通过单调递增做
        """
        res = []
        x, y = 1, 1000
        
        while x <= 1000 and y >= 1:
            value = customfunction.f(x, y)
            # 因为f(x, y)大于z，所以所有x' > x 的f(x', y)都大于z，所以y-=1
            if value > z:
                y -= 1
            elif value < z:
                x += 1
            else:
                res.append([x, y])
                x += 1
                y -= 1
        
        return res
                
        