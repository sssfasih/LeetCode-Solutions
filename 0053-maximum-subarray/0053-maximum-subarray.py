class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  
        maxx = 0
        count = 0
        for i in range(len(nums)):         
            count+= nums[i]
            if count>maxx:
                maxx=count
            if count < 0:
                count = 0

        if maxx == 0:
            maxx = 99999 #max will turn into min, will find min possible num
            for i in range(len(nums)):
                if abs(nums[i]) < abs(maxx):
                    maxx = nums[i]

        return maxx
                