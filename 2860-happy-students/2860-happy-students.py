class Solution:
    def countWays(self, nums: List[int]) -> int:
        # sort and try 所有的情况
        # 选择人数是固定的情况下，方案数也是固定的
        nums.sort()
        # 所以排序之后左边的都要选，右边的都不能选
        # 所以需要满足 nums[i−1] < i < nums[i]
        
        # 一个学生都不选
        ans = nums[0] > 0
        
        for i, (x, y) in enumerate(pairwise(nums), 1):
            if x < i < y:
                ans += 1
        
        # 一定都选的情况，所有情况都选
        return ans + 1