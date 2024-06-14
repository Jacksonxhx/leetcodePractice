class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        因为要避免超时，所以用前缀合+哈希表做
        用哈希表统计不同前缀合出现的次数
        """
        # 初始化，前缀合0出现了1次
        prefix_fre = {0:1}
        
        # 初始化前缀合
        prefix_sum = 0
        
        # 初始化结果
        res = 0
        
        # 遍历nums
        for num in nums:
            # 首先更新一直追踪的前缀和
            prefix_sum += num
            
            # 然后处理base case
            # 因为要找到和是k的subarray，就是找到当前num - k == prefix_sum的那一个hash存的数量，加到res上
            if prefix_sum - k in prefix_fre:
                res += prefix_fre[prefix_sum - k]
            
            if prefix_sum not in prefix_fre:
                prefix_fre[prefix_sum] = 1
            else:
                prefix_fre[prefix_sum] += 1
        
        return res