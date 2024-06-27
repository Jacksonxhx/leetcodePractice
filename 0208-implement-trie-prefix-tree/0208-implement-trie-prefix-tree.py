class Node:
    def __init__(self):
        # 因为都是小写，每个节点可以存26个字母的一个
        self.children = [None for _ in range(26)]
        self.isEnd = False

class Trie:

    def __init__(self):
        # root没有值
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if cur.children[index] is None:
                # 如果没有，创造一个
                cur.children[index] = Node()
            # 更新cur到下一个对应的位置
            cur = cur.children[index]
        # 做一个标记
        cur.isEnd = True 

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
            
        # 确保是到了单词的结尾
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)