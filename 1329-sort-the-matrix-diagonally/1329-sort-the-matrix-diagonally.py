class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        因为每一条diagonal的difference都一样 == i - j，用这个作为index
        hasht 存
        """
        hasht = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                hasht[i - j].append(mat[i][j])
        
        for key in hasht:
            hasht[key].sort(reverse=True)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = hasht[i - j][-1]
                hasht[i - j].pop()
        
        return mat