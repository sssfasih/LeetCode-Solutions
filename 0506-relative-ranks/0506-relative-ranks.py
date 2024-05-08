class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hm = {}
        for i in range(len(score)):
            hm[score[i]] = i
        score.sort(reverse = True)
        res = [""]*len(score)
        for i in range(len(score)):
            if  i == 0:
                res[hm[score[i]]] = "Gold Medal"
            elif i == 1:
                res[hm[score[i]]] = "Silver Medal"
            elif i == 2:
                res[hm[score[i]]] = "Bronze Medal"
            else:
                res[hm[score[i]]] = str(i+1)
        return res