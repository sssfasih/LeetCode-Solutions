class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Python set is Hashset, and allows O(1) Operations like Hashtables
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False