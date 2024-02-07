class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # n做法：遍历一遍，用dict记录以nums为key，index为value
        res = dict()
        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]] = [i]
            else:
                res[nums[i]].append(i)
        
        for key, value in res.items():
            if len(value) >= 2:
                for i in range(len(value) - 1):
                    tmp = value[i + 1] - value[i]
                    if tmp <= k:
                        return True
                    
        return False
        