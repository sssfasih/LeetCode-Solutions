class Solution:
    def makeGood(self, s: str) -> str:
        i=0
        while i<len(s)-1:
            if (s[i] != s[i+1] and s[i].lower() == s[i+1].lower()):
                s= s[:i:] +s[i+2::]
                if i>0:
                    i-=1 
                continue
            
            i+=1
        return s
        