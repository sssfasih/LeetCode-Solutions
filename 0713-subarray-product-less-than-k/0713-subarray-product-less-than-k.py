class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #sliding window
        i,j = 0,0
        ans=0
        temp = 1
        nums_len = len(nums)
        while j < nums_len:

            # process
            temp *= nums[j]
            
            # under condition negate process
            while temp >= k and i <=j:
                temp /= nums[i]
                i+=1
            
            #ALWAYS mantain impact and increaes j
            ans += j-i+1
            j+=1
            
        return ans
        