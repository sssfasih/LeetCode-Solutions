class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lsorted = []
        l = []
        for i in range(len(strs)):
            a = list(strs[i])
            a.sort()
            flag = False
            j=0
            for j in range(len(lsorted)):
                if lsorted[j] == a:
                    l[j].append(strs[i])
                    flag = True
                    break
            if flag == False:
                lsorted.append(a)
                l.append([strs[i]])
                                
        
        return l