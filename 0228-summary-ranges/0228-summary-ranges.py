class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        st = 0
        ed = 0
        for i in range(len(nums)):
            #处理越界情况
            if i == len(nums) - 1:
                ed = i
                if st == ed:
                    res.append(str(nums[st]))
                else:
                    str_res = str(nums[st]) + "->" + str(nums[ed])
                    res.append(str_res)
                break
            
            k = i + 1
            if nums[k] == nums[i] + 1:
                i += 1
            else:
                ed = i
                if st == ed:
                    res.append(str(nums[st]))
                else:
                    str_res = str(nums[st]) + "->" + str(nums[ed])
                    res.append(str_res)
                st = i + 1
        return res