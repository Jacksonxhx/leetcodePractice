class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        原地hash，因为range是[1, n + 1]，把当前nums当作一个hash，index是对应的数，找到index不等于value的地方就是缺少的
        """
        size = len(nums)
        
        for i in range(size):
            # 只对于nums[i]在范围内的数，nums[i]应该被放到nums[i] - 1这个位置
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(size):
            # 如果遇不到，就证明缺这个数
            if nums[i] != i + 1:
                return i + 1
        
        # 如果都不缺。那就是少最大的那个数
        return size + 1
        