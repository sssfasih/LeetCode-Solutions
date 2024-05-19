class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            _1s = bin(i)[2::].count('1')
            if _1s == k:
                total+= nums[i]
        return total