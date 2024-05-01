class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        nums_len = len(nums)
        if nums_len==1:
            nums[0].sort()
            return nums[0]
        ans=[]
        
        for i in range(nums_len):
            for j in range(len(nums[i])):
                count = 0
                for k in range(i+1 , nums_len):
                    if nums[i][j] in nums[k]:
                        count+=1
                        
                    if count == nums_len-1:
                        ans.append(nums[i][j])
        ans.sort()
        return ans
                