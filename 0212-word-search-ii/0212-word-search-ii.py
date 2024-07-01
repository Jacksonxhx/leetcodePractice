class Node:
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.isEnd = True
        cur.word = word
    
    def searchStartWith(self, prefix: str):
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        
        return cur is not None and cur.isEnd
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        先用trie存所有的words，然后上下左右四个方向依次遍历board中的每一个字符
        用backtrack，如果prefix不在trie，直接continue
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        # 上下左右四个方向
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(board)
        cols = len(board[0])
        
        res = set()
        path = []
        # 像这种有重复的就用index记录是否有访问过
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def backtrack(row, col, node):
            if node.isEnd:
                res.add(node.word)
            
            visited[row][col] = True
            path.append(board[row][col])
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    # 环顾四周找到在prefix上的下一个ch
                    next_node = node.children.get(board[nr][nc])
                    if next_node:
                        backtrack(nr, nc, next_node)
            
            # 恢复现场
            visited[row][col] = False
            path.pop()
        
        for row in range(rows):
            for col in range(cols):
                start_node = trie.root.children.get(board[row][col])
                if start_node:
                    backtrack(row, col, start_node)
        
        return list(res)
            