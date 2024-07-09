class NumArray:

    def __init__(self, nums: List[int]):
        length = len(nums)
        self.prefix = [nums[0]] * length
        for i in range(1, length):
            self.prefix[i] = self.prefix[i - 1] + nums[i]
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)