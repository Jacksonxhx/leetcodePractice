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
                # 
                if i  > start_index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()
        
        backtracking(0)
        return res
            