class Solution:
    def numWays(self, s: str) -> int:
        total_ones = s.count('1')
        n = len(s)
        
        if total_ones % 3 != 0:
            return 0
        
        # 遇到没有1的情况
        if total_ones == 0:
            return ((len(s) - 1) * (len(s) - 2) // 2) % (10**9 + 7)
        
        ones_per_part = total_ones // 3
        
        first_cut_start = first_cut_end = second_cut_start = second_cut_end = -1
        count = 0
        
        for i, char in enumerate(s):
            if char == '1':
                count += 1
                if count == ones_per_part:
                    first_cut_start = i
                # 找到第一根结束位置
                if count == ones_per_part + 1:
                    first_cut_end = i
                if count == 2 * ones_per_part:
                    second_cut_start = i
                # 找到第二根结束位置
                if count == 2 * ones_per_part + 1:
                    second_cut_end = i
    
        first_cut_ways = first_cut_end - first_cut_start
        second_cut_ways = second_cut_end - second_cut_start
        
        return (first_cut_ways * second_cut_ways) % (10**9 + 7)