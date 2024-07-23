class Solution:
    def rotate(self, mat):
        transpose = [list(row) for row in zip(*mat)]
        
        rotate = [row[::-1] for row in transpose]
        
        return rotate
    
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        
        # 最多检查3次
        for _ in range(3):
            mat = self.rotate(mat)
            
            if mat == target:
                return True
        
        return False