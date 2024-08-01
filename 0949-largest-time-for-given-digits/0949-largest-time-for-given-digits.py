class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        """
        4位数组合，排序
        """
        max_time = -1
        # 枚举所有可能的时间组合
        for h, i, j, k in itertools.permutations(arr):
            hours = h * 10 + i
            minutes = j * 10 + k
            if 0 <= hours < 24 and 0 <= minutes < 60:
                max_time = max(max_time, hours * 60 + minutes)
        
        if max_time == -1:
            return ""
        else:
            return f"{max_time // 60:02}:{max_time % 60:02}"