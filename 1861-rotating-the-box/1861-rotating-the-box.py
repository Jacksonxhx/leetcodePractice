class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        先模拟再转
        """
        for i in range(len(box)):
            # 用一个constant记录最右边的空位子
            last_empty_position = len(box[0]) - 1
            # 从右往左遍历每一行
            for j in range(len(box[0]) - 1, -1, -1):
                if box[i][j] == '*':
                    # 更新空位位置为障碍物的左边一格
                    last_empty_position = j - 1 
                elif box[i][j] == '#':
                    box[i][j], box[i][last_empty_position] = box[i][last_empty_position], box[i][j] 
                    # 更新空位位置
                    last_empty_position -= 1  
            
        # 矩阵顺时针旋转90度
        n, m = len(box), len(box[0])
        rotated_box = [[None] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                rotated_box[j][n-1-i] = box[i][j]
        
        return rotated_box