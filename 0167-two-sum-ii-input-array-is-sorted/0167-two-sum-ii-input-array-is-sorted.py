class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #定义两个指针，一个从左往右一个从右往左
        left, right = 0, len(numbers) - 1
        
        #双指针算法
        '''
        1. 一个从左往右，一个从右往左
        2. 因为是升序序列，所以当sum>target意味着右边的大了，所以right -= 1
        3. 反之就是左边的小了，left += 1
        4. 把双重循环变成O(n)
        '''
        while left < right:
            sumn = numbers[left] + numbers[right]
            if sumn == target:
                return [left + 1, right + 1]
            elif sumn > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]