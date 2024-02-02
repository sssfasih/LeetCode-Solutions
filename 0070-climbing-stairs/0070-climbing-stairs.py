class Solution:

    cache = {}
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n == 1:
            val = 1
        elif n == 2:
            val = 2
        elif n> 2:
            val = self.climbStairs(n-1) + self.climbStairs(n-2)
            
        self.cache[n] = val    
        return val