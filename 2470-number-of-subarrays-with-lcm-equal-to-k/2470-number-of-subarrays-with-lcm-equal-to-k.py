class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        """
        若nums[j] > k，直接i = j + 1
        """
        ans, n = 0, len(nums)
        for i in range(n):
            res = 1
            for j in range(i, n):
                res = lcm(res, nums[j])
                if k % res: 
                    i = j
                    break 
                if res == k: ans += 1
                    
        return ans

            