class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        for i in range(len(s)-1,-1,-1):
            if s[i].lower() in 'abcdefghijklmnopqrstuvwxyz':
                counter +=1
            elif s[i] == ' ' and counter > 0:
                return counter
        
        return counter

        