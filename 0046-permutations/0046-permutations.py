class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        两者本质相同，实现方法不同
        1. DFS全排列
            可以画出一个决策树，然后按照深度优先搜索，找到最底部
        2. 回溯backtracking
        """
        res: list[list[int]] = [] # 存放最终结果
        path: list = [] # 存放当前结果
        
        def backtracking(nums: list[int]) -> None:
            # base case，当走到最底层，return
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            # 进入下一层决策树，枚举可选元素列表
            for i in range(len(nums)):
                # 当该元素没被使用过
                if nums[i] not in path:
                    # path加入元素
                    path.append(nums[i])
                    # 回溯搜索下面的
                    backtracking(nums)
                    # 回溯
                    path.pop()
                    
        # 入口
        backtracking(nums)
        return res
        