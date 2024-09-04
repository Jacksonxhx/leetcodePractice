class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        prefix = [0] * (n + 1)
        
        # 用差分算出前缀合
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + differences[i - 1]
        
        res = (upper - lower + 1) - (max(prefix) - min(prefix))
        
        return res if res > 0 else 0