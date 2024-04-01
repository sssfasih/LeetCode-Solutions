class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if s[i-1] == ' ':
                count=0
            count+=1
        return count

        