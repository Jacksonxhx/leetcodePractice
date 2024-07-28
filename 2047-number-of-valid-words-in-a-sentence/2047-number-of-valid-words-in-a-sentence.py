class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        punctuation = '!.,'
        res = 0
        
        for word in words:
            cnt_hyphen = 0
            cnt_punct = 0
            valid = True

            for i, ch in enumerate(word):
                if ch.isdigit():
                    valid = False
                    break
                if ch == '-':
                    cnt_hyphen += 1
                    if cnt_hyphen > 1 or i == 0 or i == len(word) - 1 or not (word[i - 1].isalpha() and word[i + 1].isalpha()):
                        valid = False
                        break
                if ch in punctuation:
                    cnt_punct += 1
                    if cnt_punct > 1 or i != len(word) - 1:
                        valid = False
                        break

            if valid:
                res += 1
        
        return res
                    