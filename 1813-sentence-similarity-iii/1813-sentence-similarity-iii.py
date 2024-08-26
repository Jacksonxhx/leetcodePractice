from collections import deque

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence2) > len(sentence1):
            sentence1, sentence2 = sentence2, sentence1
        
        queue1 = deque(sentence1.split())
        queue2 = deque(sentence2.split())
        
        i, j = 0, len(queue1) - 1

        while queue2 and i <= j and queue1[i] == queue2[0]:
            queue2.popleft()
            i += 1
        
        while queue2 and i <= j and queue1[j] == queue2[-1]:
            queue2.pop()
            j -= 1
        
        return len(queue2) == 0
        
        
        