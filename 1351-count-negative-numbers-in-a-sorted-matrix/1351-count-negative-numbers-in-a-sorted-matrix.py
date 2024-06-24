class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in grid:
            l, r = 0, len(i) - 1
            while l <= r:
                mid = (l + r) // 2
                if i[mid] < 0:
                    r = mid - 1
                else:
                    l = mid + 1
            cnt += len(i) - l
        return cnt