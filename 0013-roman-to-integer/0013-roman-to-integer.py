class Solution:
    def romanToInt(self, s: str) -> int:
        # O(n) Approach with Constant Space
        numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        # To avoid negative indexing of list
        ans += numerals[s[0]]
        for i in range(1,len(s)):
            if s[i] == 'V' and s[i-1] == 'I':
                # we subtract 1 and add 4
                ans+=3
            elif s[i] == 'X' and s[i-1] == 'I':
                ans+=8
            elif s[i] == 'L' and s[i-1] == 'X':
                ans+=30
            elif s[i] == 'C' and s[i-1] == 'X':
                ans+=80
            elif s[i] == 'D' and s[i-1] == 'C':
                ans+=300
            elif s[i] == 'M' and s[i-1] == 'C':
                ans+=800
            else:
                ans += numerals[s[i]]
        return ans
            
        