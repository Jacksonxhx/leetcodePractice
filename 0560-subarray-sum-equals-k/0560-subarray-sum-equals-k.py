class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        用前缀和和哈希表做
        '''
        pre_dic = {0: 1}
        pre_sum = 0
        cnt = 0
        for num in nums:
            pre_sum += num
            # 统计有多少个前缀和为pre_sum - k
            if pre_sum - k in pre_dic:
                cnt += pre_dic[pre_sum - k]
            # 收集所有的前缀合出现的次数
            if pre_sum in pre_dic:
                pre_dic[pre_sum] += 1
            else:
                pre_dic[pre_sum] = 1
        return cnt