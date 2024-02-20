class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_length = len(nums)
        lst = [i for i in range(nums_length+1)]

        for i in range(nums_length):
            lst[nums[i]] = None
        
        for i in range(nums_length+1):
            if lst[i]:
                return lst[i]
            
            
        
        
        return lst[0]
            
        