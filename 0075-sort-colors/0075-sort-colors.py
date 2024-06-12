class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] >= nums[j]:
                    temp=nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    