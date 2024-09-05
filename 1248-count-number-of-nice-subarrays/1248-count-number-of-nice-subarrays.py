class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # prefix做
        res = 0
        # 记录每个位置的“奇数个数前缀和”的出现次数
        prefix = defaultdict(int)
        # 前缀奇数个数为 0 的次数是 1 次
        prefix[0] = 1
        
        # 当前遍历位置之前的奇数个数
        odd_cnt = 0
        
        for num in nums:
            if num % 2 == 1:
                odd_cnt += 1
            
            # 找到位置p使得从位置 p+1 到当前的位置恰好有 k 个奇数
            if odd_cnt - k in prefix:
                res += prefix[odd_cnt - k]
            
            # 相当于统计odd_cnt下有多少个subarray
            prefix[odd_cnt] += 1
        
        return res