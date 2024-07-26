class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # store prefix of xor for arr
        for i in range(len(arr) - 1):
            arr[i + 1] ^= arr[i]
        
        # 如果i == 0，那答案就是arr[j]
        # 如果i不是0，那就是arr[j] ^ arr[i - 1]
        return [arr[j] ^ arr[i - 1] if i else arr[j] for i, j in queries]