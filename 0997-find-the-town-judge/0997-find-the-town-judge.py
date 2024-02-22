class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        array = [i+1 for i in range(n)]
        hashtable = {i+1:0 for i in range(n)}
        for i in range(len(trust)):
            hashtable[trust[i][1]] += 1
            array[trust[i][0]-1] = False
        
        for i in range(len(array)):
            if array[i] and hashtable[array[i]] ==n-1:
                return array[i]
        return -1
        