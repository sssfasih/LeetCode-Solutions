class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        xl = len(x)-1
        for i in range(xl//2+1):
            if x[i] == x[xl]:
                xl-=1
                pass
            else:
                return False
        return True
        