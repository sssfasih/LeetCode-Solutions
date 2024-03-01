class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        for i in range(len(s)):
            if s[i] == '1':
                count+= 1
        return ''.join('1'*(count-1))+'0'*(len(s)-count)+'1'
        