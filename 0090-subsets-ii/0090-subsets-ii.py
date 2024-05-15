class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        回溯算法
        '''
        res = []
        path = []
        nums.sort() # 先排序，方便处理
        
        def backtracking(start_index):
            res.append(path[:])
            for i in range(start_index, len(nums)):
                # 当现在这一位和上一位一样，那之后的都会重复
                # 因为之前排过序了，所以可以这么操作
                # 举个例子 [1,2,2,3], [1,2, ,3]和[1, ,2,3]是一样的
                if i  > start_index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()
        
        backtracking(0)
        return res
            