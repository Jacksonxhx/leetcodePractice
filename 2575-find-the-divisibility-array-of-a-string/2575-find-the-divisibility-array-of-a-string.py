class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        """
        边计算边取模，避免太大
        """
        res = []
        x = 0
        
        # 把word里的每个字符变成int
        for d in map(int, word):
            # 更新, number theory
            x = (x * 10 + d) % m
            res.append(0 if x else 1)
            
        return res