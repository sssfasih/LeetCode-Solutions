class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                if counter > 0:
                    return counter
                continue
            counter +=1
        
        return counter

        