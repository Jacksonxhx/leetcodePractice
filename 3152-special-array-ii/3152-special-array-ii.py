class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        """
        把nums分成non-intersected的continuous subarray，然后看each query是否<= 这些subarray的start和end，如果不是false
        """
        # 0前后parity一样，1不一样
        parity = list(accumulate((x % 2 == y % 2 for x, y in pairwise(nums)), initial=0))
        print(parity)
        return [parity[start] == parity[end] for start, end in queries]
        
        