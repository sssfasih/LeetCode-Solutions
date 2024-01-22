class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst = [0] * (n + 1)
        missing, duplicate = 0, 0

        for each_num in nums:
            lst[each_num] += 1

        for i in range(1, len(lst)):
            if lst[i] == 2:
                duplicate = i
            if lst[i] == 0:
                missing = i

        return [duplicate, missing]