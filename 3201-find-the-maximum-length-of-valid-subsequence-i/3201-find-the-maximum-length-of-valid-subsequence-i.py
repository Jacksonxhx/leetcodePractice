class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # 前后要么都是奇偶，要么是偶偶 奇奇
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        res_even = 0
        res_odd = 0
        for num in nums:
            if num == 0:
                res_even += 1
            else:
                res_odd += 1
        
        res_odd_even = 1  
        res_even_odd = 1  
        
        last_odd_even = nums[0]
        last_even_odd = nums[0]
        
        for i in range(1, n):
            if nums[i] != last_odd_even:
                res_odd_even += 1
                last_odd_even = nums[i]
            
            if nums[i] != last_even_odd:
                res_even_odd += 1
                last_even_odd = nums[i]
        
        # 返回最长的子序列
        return max(res_even, res_odd, res_odd_even, res_even_odd)