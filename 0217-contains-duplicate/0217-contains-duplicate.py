class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Python set is Hashset, and allows O(1) Operations like Hashtables
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] in hashtable:
                return True
            hashtable[nums[i]]=1
        return False