class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                ans.append(abs(nums[i])) 
            nums[abs(nums[i])-1] *= -1
        
        return ans