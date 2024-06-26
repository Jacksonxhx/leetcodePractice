class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums: List[int], target: int) -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l # 它指向第一个大于或等于目标值的位置
        
        def findRight(nums: List[int], target: int) -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r # 它指向最后一个小于或等于目标值的位置
        
        left = findLeft(nums, target)
        right = findRight(nums, target)
        
        if left <= right and left < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        return [-1, -1]