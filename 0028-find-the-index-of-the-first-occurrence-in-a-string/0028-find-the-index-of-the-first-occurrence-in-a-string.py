class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and len(needle) <= len(haystack)-i:
                for j in range(len(needle)):
                    if haystack[i+j] == needle[j]:
                        flag = True
                    else:
                        flag =False
                        break                
                if flag==True:
                    return i
        return -1
        