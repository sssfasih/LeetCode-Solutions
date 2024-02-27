class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        ans=0
        while amount[2] > 0:
            ans +=1 
            amount[2] -= 1
            amount[1]-=1
            amount.sort()
        return ans