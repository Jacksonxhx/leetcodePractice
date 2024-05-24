class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        用sliding window维护一个序列
        先用hashmap存好words里，每个单词出现的数量
        '''
        if not s or not words:
            return []
        
        word_length = len(words[0])
        word_count = len(words)
        substring_length = word_length * word_count
        word_map = Counter(words)
        result = []
        
        for i in range(word_length):
            left, right = i, i
            curr_map = Counter()
            count = 0
            
            while right + word_length <= len(s):
                word = s[right: right + word_length]
                right += word_length
                
                # 当在这个concate里面开始
                if word in word_map:
                    curr_map[word] += 1
                    count += 1
                
                    # 如果某个单词的计数超过了word_map中的次数，调整左指针
                    while curr_map[word] > word_map[word]:
                        left_word = s[left:left + word_length]
                        curr_map[left_word] -= 1
                        count -= 1
                        left += word_length

                    if count == word_count:
                        result.append(left)
                        
                else:
                    curr_map.clear()
                    count = 0
                    left = right
                    
        return result