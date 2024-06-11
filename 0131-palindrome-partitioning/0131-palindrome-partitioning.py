class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []
        
        def backtracking(start: int):
            # 用start当作index记录
            if start == len(s):
                # 要append[:]，是副本而不是地址
                res.append(partition[:])
                return
            
            # 用end记录单一palindrome substring的end
            for end in range(start + 1, len(s) + 1):
                if self.is_palindrome(s[start:end]):
                    partition.append(s[start:end])
                    # 递归
                    backtracking(end)
                    # 回溯
                    partition.pop()
        
        backtracking(0)
        return res
    
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
                
            