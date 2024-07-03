class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        result = []
        current_line = []
        current_line_length = 0
        
        for word in words:
            # 新加入一个词会不会超, len(current_line)就是空格数量
            if current_line_length + len(word) + len(current_line) > maxWidth:
                # 剩下几个空格，处理空格分布
                for i in range(maxWidth - current_line_length):
                    # (len(current_line) - 1 or 1)需要分几个空
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                
                # 重置
                result.append(''.join(current_line))
                current_line = []
                current_line_length = 0
            
            # 没超的话append
            current_line.append(word)
            current_line_length += len(word)
        
        result.append(' '.join(current_line).ljust(maxWidth))
        return result