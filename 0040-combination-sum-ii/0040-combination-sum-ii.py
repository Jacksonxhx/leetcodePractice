class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        
        def backtrack(start, target, candidates):
            # 遇到结果了
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return
        
            for i in range(start, len(candidates)):
                # 遇到重复的pass
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], candidates)
                path.pop()
        
        backtrack(0, target, candidates)
        
        return res