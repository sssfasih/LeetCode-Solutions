class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_len = len(nums)
        i=0
        while i < nums_len:
            if nums[i] < 1 or nums[i] > nums_len:
                nums[i] = nums_len+1
            i+=1

        for i in range(nums_len):
            if abs(nums[i]) != nums_len+1 and nums[i] <= nums_len:
                if nums[abs(nums[i])-1] > 0:
                    nums[abs(nums[i])-1] *= -1
                
        for i in range(nums_len):
            if nums[i] > 0:
                return i+1
        
        return nums_len+1
        

        