class Solution:
    def countSubstrings(self, s: str) -> int:
        string = ''
        count = 0
        for i in range(len(s)):
            for j in range(len(s)):
                string = s[i:j+1]
                if string and string == string[::-1]:
                    count += 1
        return count
        