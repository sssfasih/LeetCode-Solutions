class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = bin(n)[2:]
        prev = None
        for i in range(len(a)):
            if a[i] != prev:
                prev = a[i]
                continue
            else:
                return False
            
        return True