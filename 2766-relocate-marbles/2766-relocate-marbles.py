class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        hasht = set(nums)
        n = len(moveFrom)        
        
        for i in range(n):
            hasht.remove(moveFrom[i])
            hasht.add(moveTo[i])
            
        return sorted(list(hasht))