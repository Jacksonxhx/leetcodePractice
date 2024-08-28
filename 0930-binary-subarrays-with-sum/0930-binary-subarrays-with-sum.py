class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # 使用前缀合配合哈希表
        # 维护一个哈希表 prefix_sum_count 来记录每个前缀和出现的次数
        # 设当前前缀和为 current_sum，如果在某个位置 j，有 current_sum - goal 在哈希表中出现过，这意味着从某个位置到 j 的子数组的和正好为 goal
        # 每当我们找到一个这样的子数组时，就增加计数器。
        
        # 构建hash，init 0出现了1次
        prefix_sum_count = {0: 1}
        current_sum, res = 0, 0
        
        for num in nums:
            # 更新前缀合
            current_sum += num
            
            # 检查之前是否出现过从j位置到当前和是goal的，res加上出现满足条件的j位置的数量
            if current_sum - goal in prefix_sum_count:
                res += prefix_sum_count[current_sum - goal]
            
            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1
        
        return res