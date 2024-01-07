class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        summ = 0
        for i in range(len(nums)):
            
            summ += nums[i]

            if i > 0:
                if nums[i] == nums[i-1] + 1:
                    pass
                else:
                    summ -= nums[i]
                    break



        while True:
            if summ not in nums:
                return summ
            else:
                summ += 1
            
                