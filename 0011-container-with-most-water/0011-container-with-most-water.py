class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i, j = 0, len(height) - 1
        maxv = 0
        
        while i <= j:
            length = j - i
            
            if height[i] < height[j]:
                maxh = height[i]
                i += 1
            else:
                maxh = height[j]
                j -= 1
            
            if (length * maxh > maxv):
                maxv = (length) * maxh
                
        return maxv