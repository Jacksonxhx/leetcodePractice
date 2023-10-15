class Solution:
    def isPalindrome(self, s: str) -> bool:
        #先把所有的都小写
        str = s.lower()
        #创造一个字符数组
        str_array = []
        #遍历一遍小写字符串，把所有字母数字都加入到字符数组中
        for c in str:
            if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57): 
                str_array.append(c)
        #定义双指针，一个从前往后，一个从后往前
        i = 0
        j = len(str_array) - 1
        #判断前后是否一样
        while i < j:
            if str_array[i] == str_array[j]:
                i += 1
                j -= 1
            else: return False
        return True