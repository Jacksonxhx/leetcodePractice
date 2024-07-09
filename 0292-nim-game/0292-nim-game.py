class Solution:
    def canWinNim(self, n: int) -> bool:
        # 4必输 567都能凑4赢 8必输，所以4的倍数必输
        if n % 4 == 0:
            return False
        return True