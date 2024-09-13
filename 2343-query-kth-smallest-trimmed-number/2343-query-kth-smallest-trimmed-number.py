class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n = len(nums[0])
        ans = []
        
        for k, trim in queries:
            tmp = nums
            res = [int(x[n-trim:n]) for x in tmp]
            ids = sorted(range(len(res)), key=lambda i: res[i])
            
            ans.append(ids[k - 1])
        
        return ans