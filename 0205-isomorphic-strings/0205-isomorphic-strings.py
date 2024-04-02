class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_ref = defaultdict(str)
        t_ref = defaultdict(str)
        for i in range(len(s)):
            if s_ref[s[i]] != '' and s_ref[s[i]] != t[i]:
                return False
            if t_ref[t[i]] != '' and t_ref[t[i]] != s[i]:
                return False

            s_ref[s[i]] = t[i]
            t_ref[t[i]] = s[i]

        return True