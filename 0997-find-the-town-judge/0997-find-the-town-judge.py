class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = [False for i in range(n)]
        num_trusted = [0 for i in range(n)]
        for i in range(len(trust)):
            num_trusted[trust[i][1]-1] += 1
            trusting[trust[i][0]-1] = True
        
        for i in range(len(trusting)):
            if trusting[i] == False and num_trusted[i] ==n-1:
                print(i+1)
                return i+1
        return -1
        