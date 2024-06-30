class Node:
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        # 以这个prefix开头有什么词
        self.words = []
class Trie:
    def __init__ (self):
        self.root = Node()
    
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
            cur.words.append(word)
            
        cur.isEnd = True
    
    def startsWith(self, prefix):
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True
    
    def searchStartsWith(self, prefix):
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return []
            cur = cur.children[ch]
        # 最后范围以prefix开头的words列表
        return cur.words
            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        用trie数组存prefix和词
        """
        trie = Trie()
        res = []
        for product in products:
            trie.insert(product)
        
        for i in range(len(searchWord)):
            if trie.startsWith(searchWord[:i + 1]):
                tmp = trie.searchStartsWith(searchWord[:i + 1])
                res.append(sorted(tmp)[:3])
            else:
                res.append([])
        
        return res
                