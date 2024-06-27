class Node:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if cur.children[index] is None:
                cur.children[index] = Node()
            cur = cur.children[index]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(cur, i):
            if i == len(word):
                return cur.isEnd
            elif word[i] == '.':
                for child in cur.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
            else:
                index = ord(word[i]) - ord('a')
                child = cur.children[index]
                if child:
                    return dfs(child, i + 1)
                else:
                    return False
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)