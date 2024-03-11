class Solution:
    def countElements(self, nums: List[int]) -> int:
        lc= 0
        hc=0
        l=999999
        h=-999999
        for i in range(len(nums)):
            if nums[i] == l:
                lc+=1
            elif nums[i] < l:
                l=nums[i]
                lc=1
            if nums[i] == h:
                hc+=1
            elif nums[i] > h:
                h=nums[i]
                hc=1
                        
        if l == h: return 0
        return len(nums)-lc-hc