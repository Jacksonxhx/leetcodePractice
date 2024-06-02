class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        构建一个hash table，按照横竖建立hash，如果一样，res ++
        '''
        cnt = 0
        hasht = dict()
        
        # 找横过来的
        for i in range(len(grid)):
            # 用逗号避免一样的数字
            tmp_str = ",".join(map(str, grid[i])) # 把每一位变成str
            if tmp_str not in hasht:
                hasht[tmp_str] = 1
            else:
                hasht[tmp_str] += 1
            print(tmp_str)
        
        # 找竖过来的
        for i in range(len(grid)):
            tmp_str = ",".join(str(grid[j][i]) for j in range(len(grid)))
            if tmp_str in hasht:
                cnt += hasht[tmp_str]
        
        return cnt