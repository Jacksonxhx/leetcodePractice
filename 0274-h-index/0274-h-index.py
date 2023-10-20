class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        size = len(citations)
        count = 0
        for i in range(size-1, -1, -1):
            if (count >= citations[i]):
                return count
            count += 1
        return count