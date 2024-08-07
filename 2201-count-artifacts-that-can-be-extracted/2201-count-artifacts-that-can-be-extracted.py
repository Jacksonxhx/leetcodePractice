class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        # 存所有的dig
        dig_map = [[False for _ in range(n)] for _ in range(n)]
        for dx, dy in dig:
            dig_map[dx][dy] = True
        
        res = 0
        # 只能存4个
        for art in artifacts:
            existed = True
            for i in range(art[0], art[2] + 1):
                for j in range(art[1], art[3] + 1):
                    if dig_map[i][j] == False:
                        existed = False
                        break
                if not existed:
                    break
            if existed:
                res += 1
        
        return res
                
            
        