class Solution:
    def arraySign(self, nums: List[int]) -> int:
        positive = True
        for i in range(len(nums)):
            if nums[i] < 0:
                if positive:positive=False
                else: positive=True
            elif nums[i]==0:
                return 0
        if positive:return 1
        return -1