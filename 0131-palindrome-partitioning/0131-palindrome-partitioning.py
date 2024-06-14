class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        回溯算法找s所有对应的substring然后判断是否回文
        """
        # 初始化res
        res = []
        path = []
        
        def backtracking(start: int):
            if start == len(s):
                res.append(path[:])
                return
            
            # 用end记录单一palindrome substring的end
            # 枚举所有的可能性
            for end in range(start + 1, len(s) + 1):
                # 给出判断条件
                if self.is_palindrome(s[start:end]):
                    # 满足条件，加入path
                    path.append(s[start:end])
                    # 回溯
                    backtracking(end)
                    # 清理现场
                    path.pop()
        
        backtracking(0)
        return res
    
    def is_palindrome(self, s) -> bool:
        return s == s[::-1]
                
            