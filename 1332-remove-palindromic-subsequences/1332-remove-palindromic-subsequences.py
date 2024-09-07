class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # 因为只会有a或者b，所以max_steps只有2
        # 所以只需要判断是不是palindomic，如果是，return 1 else 2
        return 1 if s == s[::-1] else 2
                