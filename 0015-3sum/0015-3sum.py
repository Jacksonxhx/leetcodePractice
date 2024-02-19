class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to make two-pointer technique feasible
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:  # Skip duplicate for i
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # Skip duplicates for left
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # Skip duplicates for right
                        right -= 1
                    left += 1
                    right -= 1
        return res
            