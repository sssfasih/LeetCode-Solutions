class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        sett = set()
        ans = set()
        for i in range(len(nums1)):
            sett.add(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] in sett:
                ans.add(nums2[i]) 
        return ans
                
        
        