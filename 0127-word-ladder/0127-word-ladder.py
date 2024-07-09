from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        其实是一个图，每个wordlist里差一个字的就是一个连接，构成一个图，然后找最短路
        """
        if not wordList or endWord not in wordList:
            return 0
        word_set = set(wordList)
        if beginWord in word_set:
            word_set.remove(beginWord)
            
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            
            # 遍历词里的每个字母
            for i in range(len(word)):
                # 每个字母遍历26个字母
                for j in range(26):
                    new_word = word[:i] + chr(ord('a') + j) + word[i + 1:]
                    # 如果在，bfs到那一个
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, level + 1))
                        
        return 0