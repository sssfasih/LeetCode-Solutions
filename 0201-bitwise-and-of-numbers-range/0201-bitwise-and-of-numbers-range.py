class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = right

        while(right > left):
            ans = right & (right-1)
            right = ans
        return ans