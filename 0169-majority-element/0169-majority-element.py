class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num=int()
        count=0
        nums_length = len(nums)
        i = 0
        while i < nums_length and count <= nums_length//2:
            if count==0:
                num=nums[i]
            if nums[i]==num:
                count+=1
            else:
                count-=1
            i += 1
        return num