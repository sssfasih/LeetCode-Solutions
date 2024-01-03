class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num=int()
        count=0
        for i in range(len(nums)):
            if count==0:
                num=nums[i]
            if nums[i]==num:
                count+=1
            else:
                count-=1
        return num
                
                
            
        