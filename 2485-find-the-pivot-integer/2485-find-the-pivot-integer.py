class Solution:
    def pivotInteger(self, n: int) -> int:
        
        def summ(listt):
            count= 0
            for c in listt:
                count+=c
            return count
        
        nums = [i for i in range(1,n+1)]
        
        for i in range(len(nums)):
            if summ(nums[0:i+1:]) == summ(nums[i::]):
                return i+1
        return -1