class Solution:
    def divisorGame(self, n: int) -> bool:
        """
        抢2，如果是偶数，一直选1就稳赢；如果是奇数，奇数 - 奇数 == 偶数，稳输
        """
        return n % 2 == 0