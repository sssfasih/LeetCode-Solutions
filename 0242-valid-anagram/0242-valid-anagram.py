class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        hashmap = defaultdict(int)
        for i in range(len_s):
            hashmap[s[i]] +=1
            hashmap[t[i]] -=1
        
        for i in range(len_s):
            if hashmap[s[i]] > 0:
                return False
        return True
        