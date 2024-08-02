class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        """
        把0变成-1然后做prefix，找最近的最大值
        因为s = sum(possible)，所以前半=pre后半=s-prev
        所以要找最近的2prev > s
        """
        # 扩大s使得不用*2
        s = sum(possible) * 2 - len(possible)
        prev = 0
        # 不包括最后一个 至少玩一关
        for i, x in enumerate(possible[:-1]):
            prev += 2 if x else -2
            if prev > s:
                return i + 1
        return -1
        