class Solution:
    def gcd(self, a: int, b: int) -> int:
        # 欧几里得求最大公约数
        while b:
            a, b = b, a % b
        return a
    
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd_value = numsDivide[0]
        for num in numsDivide[1:]:
            gcd_value = self.gcd(gcd_value, num)
            if gcd_value == 1:
                break
                
        nums.sort()
        
        for i, num in enumerate(nums):
            if gcd_value % num == 0:
                return i
        
        return -1
        