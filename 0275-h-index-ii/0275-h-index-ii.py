class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations) - 1
        n = len(citations)
        
        while l < r:
            mid = (l + r) // 2
            if citations[mid] >= n - mid:
                r = mid
            else:
                l = mid + 1
        
        if citations[l] >= n - l:
            return n - l
        return 0