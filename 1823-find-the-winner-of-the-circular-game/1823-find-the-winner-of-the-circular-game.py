class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = [i for i in range(n,0,-1)]
        for i in range(n-1):
            for j in range(k-1):
                queue.insert(0,queue.pop())
            queue.pop()

        return queue[0]
    