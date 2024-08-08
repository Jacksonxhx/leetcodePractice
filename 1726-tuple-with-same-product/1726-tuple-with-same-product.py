class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        '''
        每种两两组合由4种，找到有几种22组合*4
        '''
        product_pairs = defaultdict(int)
        count = 0
        
        # 找到所有的22组合
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                # 记录乘积数量
                product_pairs[product] += 1
        
        for product in product_pairs:
            # n选2 Combination
            count += product_pairs[product] * (product_pairs[product] - 1) // 2
        
        return count * 8