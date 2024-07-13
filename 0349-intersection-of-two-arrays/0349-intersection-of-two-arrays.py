class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        def binary_search(nums: List[int], target: int) -> bool:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        # Use a set to store the intersection elements
        result_set = set()
        
        # Traverse nums1 and use binary search to check existence in nums2
        for num in nums1:
            if binary_search(nums2, num):
                result_set.add(num)
        
        # Convert the set to a list and return
        return list(result_set)