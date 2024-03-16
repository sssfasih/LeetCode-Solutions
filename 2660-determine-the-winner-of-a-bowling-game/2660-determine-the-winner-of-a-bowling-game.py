class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        s1,s2 = 0,0
        for i in range(len(player1)):
            if (i > 0 and player1[i-1])== 10 or (i > 1 and player1[i-2]) == 10:
                s1 += player1[i]*2
            else:
                s1 += player1[i]
            if (i > 0 and player2[i-1])== 10 or (i > 1 and player2[i-2]) == 10:
                s2 += player2[i]*2
            else:
                s2 +=player2[i]
        if s1>s2:return 1
        elif s2>s1:return 2
        else:return 0