class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c = Counter(str(n))
        return any(c == Counter(str(1 << i)) for i in range(30))