class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        binary search
        设置left right然后找区间
        '''
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # 先把数组分为两个部分
            # mid在数组的左半边
            if nums[mid] >= nums[left]:
                # 处理target在左半部分mid左边的情况
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                # 处理target在左半部分mid右边的情况
                else:
                    left = mid + 1
            # mid在数组的右半边
            else:
                # 处理当target在右半部分mid右边的时候
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                # 处理当target在右半部分mid左边的时候
                else:
                    right = mid - 1
        
        return -1
                
                