class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        m = max(nums)
        ans = 0
        for r in range(len(nums)):
            if nums[r] == m:
                k -= 1
            while k == 0:
                if nums[l] == m:
                    k += 1
                l += 1
            ans += l
        return ans
        