class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        双指针搭配set
        """
        visited = set()
        i, j, res, tmp = 0, 0, 0, 0

        for j in range(len(nums)):
            if nums[j] in visited:
                while nums[j] in visited:
                    visited.remove(nums[i])
                    tmp -= nums[i]
                    i += 1

            visited.add(nums[j])
            tmp += nums[j]
            res = max(res, tmp)
        
        return res
                
