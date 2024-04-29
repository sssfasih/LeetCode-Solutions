class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        a = 0
        s_len = len(s)
        t_len = len(t)
        for i in range(t_len):
            if a < s_len and s[a] == t[i]:
                a +=1 
        
        if a == s_len:
            return True
        return False
        