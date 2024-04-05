class Solution:
    def makeGood(self, s: str) -> str:
        i=0
        while i<len(s)-1:
            if s[i].islower() and s[i+1] == s[i].capitalize():
                s= s[:i:] +s[i+2::]
                if i>0:
                    i-=1 
                continue
            
            if s[i].isupper() and s[i+1] == s[i].lower():
                s= s[:i:] +s[i+2::]
                if i>0:
                    i-=1
                continue
            i+=1
        return s
        