class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1

        i, j = 0, n - 1
        while i < j:
            if s[i] == s[j]:
                prev = s[i]
                while i <= j and s[i] == prev:
                    i += 1
                while j >= i and s[j] == prev:
                    j -= 1
            else:
                break

        return max(j - i + 1, 0)