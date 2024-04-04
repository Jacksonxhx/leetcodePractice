class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        还是greedy的思想，每次跳跃需要找到下次跳跃的最远距离
        意思就是说，每一次跳跃要跳到下一次可以跳最远的那个index
        cur_end：当前最大
        max_pos：下一步最远跳到哪
        '''
        cur_end, max_pos = 0, 0
        size = len(nums)
        steps = 0
        # 因为当i = size - 1 的时候要结束，所以遍历到size - 1而不是size
        for i in range(size - 1):
            max_pos = max(max_pos, i + nums[i])
            if i == cur_end:
                cur_end = max_pos
                steps += 1
        return steps
        
        