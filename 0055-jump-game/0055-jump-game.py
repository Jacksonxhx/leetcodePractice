class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        用greedy algo做，核心思想是：如果能通过前面的某个位置j到后面的某个位置i，则[j,i]中所有的点都能到
        1. 初始化最远到达距离max = 0
        2. 遍历nums数组
        3. 如果能到达当前位置，max_i <= i，并且当前位置+当前最大跳跃长度 > max，更新max到 i + nums[i]
        4. 遍历完比较len(nums)和max关系
        """
        # 初始化max和state和size
        maxJump = 0
        canJump = False
        size = len(nums)
        # 遍历所有位置用greedy找到局部最佳，每一个i都是一个局部
        for i in range(size):
            # 如果max < i则意味着无法达到i位置
            if maxJump < i:
                break
            # 选取max和当前位置可以达到的最远距离的更大的一个
            maxJump = max(maxJump, i + nums[i])
        if maxJump >= size -1:
            canJump = True
        
        return canJump