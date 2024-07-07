class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        使用对撞指针，排序nums，然后固定i，l，r判断
        """
        nums = sorted(nums)
        size = len(nums)
        ans = 0
        
        # 固定最大的i
        for i in range(2, size):
            # r 选择i上一位
            l, r = 0, i - 1
            while l < r:
                # l 小了
                if nums[l] + nums[r] <= nums[i]:
                    l += 1
                else:
                    # l 到 r 之间都可以
                    ans += r - l
                    r -= 1
            
        return ans