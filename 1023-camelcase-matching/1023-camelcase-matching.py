class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        """
        使用迭代器查找
        """
        def up(s):
            return [c for c in s if c.isupper()]
        
        def issup(s, t):
            # 建立一个迭代器
            it = iter(t)
            # 逐个检查 s 中的每个字符 c 是否在迭代器 it 中依次出现
            return all(c in it for c in s)
        
        return [up(pattern) == up(q) and issup(pattern, q) for q in queries]