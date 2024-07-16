class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        可以转换成01背包问题
        假设positive subarray的和事sum_x, negative subarray的和是sum_y
        因为sum_x + sum_y = target, sum_x - sum_y = sum
        所以sum_x = (target + sum) // 2
        """
        # n个物品，m容量
        sum_all = sum(nums)
        
        if abs(target) > abs(sum_all) or (target + sum_all) % 2 == 1:
            return 0
        
        target = (sum_all + target) // 2
        n, m = len(nums), target
        
        # 这里dp表示的是: 填满容量为i的背包，有dp[i]种方法
        dp = [0] * (m + 1)
        dp[0] = 1
        
        # 这里v和w一样
        for num in nums:
            for j in range(m, num - 1, -1):
                # 这里拆成使用num和不使用的两种情况
                dp[j] = dp[j] + dp[j - num]
        
        return dp[m]
        