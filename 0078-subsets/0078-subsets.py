class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # 用于存储所有子集的结果列表
        path = []  # 用于跟踪当前子集的列表

        def backtracking(start_index):
            res.append(path[:])  # 将当前路径的一个副本添加到结果中
            for i in range(start_index, len(nums)):
                path.append(nums[i])  # 选择当前元素
                backtracking(i + 1)  # 递归，传入的是i+1，不是start_index+1
                path.pop()  # 撤销选择，回溯到上一步

        backtracking(0)  # 从索引0开始
        return res