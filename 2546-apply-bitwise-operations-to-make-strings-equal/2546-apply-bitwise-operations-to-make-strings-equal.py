class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # 因为有1就可以变成1或者0，但是只有0的话，没法变成1
        return ('1' in s) == ('1' in target)