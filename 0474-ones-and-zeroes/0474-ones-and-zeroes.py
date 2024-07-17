class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        size = len(strs)
        
        # dp[i][j]的定义就是，在i个0和j个1之内的最长的substr大小
        dp = [[0  for _ in range(n + 1)] for _ in range(m + 1)]
        
        for str_ in strs:
            zero_num, one_num = 0, 0
            # 统计一个str有多少个0和1
            for ch in str_:
                if ch == '0':
                    zero_num += 1
                else:
                    one_num += 1
            
            # 进行dp，但是因为是二维的所以有两层循环
            for i in range(m, zero_num - 1, -1):
                for j in range(n, one_num - 1, -1):
                    # 每次都增加一个，所以是+1
                    dp[i][j] = max(dp[i][j], dp[i - zero_num][j - one_num] + 1)
        
        
        return dp[m][n]