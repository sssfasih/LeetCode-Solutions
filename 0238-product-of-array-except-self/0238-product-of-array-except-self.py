class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numLength = len(nums)
        i,j = 1,numLength-2
        fwd = [0]*numLength
        bck = [0]*numLength
        fwd[0] = nums[0]
        bck[j+1] = nums[j+1]
        while i < numLength:
            fwd[i] = fwd[i-1]*nums[i]
            bck[j] = bck[j+1]*nums[j]
            i+=1
            j-=1
        
        ans =[]
        ans.append(bck[1])
        for i in range(1,numLength-1):
            ans.append(fwd[i-1]*bck[i+1])
        ans.append(fwd[numLength-2])
        return ans     