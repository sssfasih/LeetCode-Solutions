class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a= ''
        s_len = len(s)
        for i in range((int(s_len/2))):
            a = s[i]
            s[i] = s[s_len-1-i]
            s[s_len-i-1] = a
        
        
        return s