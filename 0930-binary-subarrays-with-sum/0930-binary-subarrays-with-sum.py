class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def atMost(nums,goal):
            i,j=0,0
            count,summ = 0,0
            while j<len(nums):
                summ += nums[j]
                while summ > goal and i <= j:
                    summ-= nums[i]
                    i+=1
                count += j-i+1
                j+=1
            return count
        return atMost(nums,goal) - atMost(nums,goal-1)