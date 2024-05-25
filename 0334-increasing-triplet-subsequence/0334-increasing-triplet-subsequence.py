class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        有a，b，c三个数的情况下满足a < b的情况下a尽可能小，b < c的情况下b尽可能小
        
        '''
        a = float('inf')
        b = float('inf')
        for i in range(len(nums)):
            # 找到i
            if nums[i] <= a:
                a = nums[i]
            # 找到j
            elif nums[i] <= b:
                b = nums[i]
            # 找到k
            else:
                return True
            
        return False