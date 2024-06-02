class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        '''
        用前缀合
        '''
        n = len(gain)
        prefix_sum = [0] * n
        prefix_sum[0] = gain[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + gain[i]
        
        if max(prefix_sum) < 0:
            return 0
        return max(prefix_sum)