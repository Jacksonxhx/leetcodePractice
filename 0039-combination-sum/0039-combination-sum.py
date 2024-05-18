class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        每次从candidate中选，target每次减去从candidate中选的数的值
        相当于每个output有n位，每一位的选项都是candidate[1, 2, 3, 4...]，然后循环n轮直到target==0为止
        '''
        res = []

        def backtracking(target, start, path):
            if target == 0:
                # 创建path副本
                res.append(list(path))
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtracking(target - candidates[i], i, path)
                path.pop()
                
        backtracking(target, 0, [])
        return res