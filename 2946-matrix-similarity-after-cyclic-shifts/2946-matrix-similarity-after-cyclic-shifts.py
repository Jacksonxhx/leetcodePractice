class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        size = len(mat[0])
        k %= size
        
        if k == 0:
            return True
            
        for row in mat:
            rotate = row[k:] + row[:k]
            if row != rotate:
                return False
        
        return True