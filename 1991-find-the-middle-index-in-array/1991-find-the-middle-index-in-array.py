#思路：
#1. 计算整个数组的和
#2. 求左边的和，若左边的和*2+当前位置的值 == sumtotal，返回当前位置
#3. 否则返回-1

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        #计算整个数组的和
        sumtotal = sum(nums)
        #求中心点
        sumleft = 0
        for i in range(len(nums)):
            if sumleft * 2 + nums[i] == sumtotal:
                return i
            else:
                sumleft += nums[i]
        #若没有找到这个点        
        return -1
        