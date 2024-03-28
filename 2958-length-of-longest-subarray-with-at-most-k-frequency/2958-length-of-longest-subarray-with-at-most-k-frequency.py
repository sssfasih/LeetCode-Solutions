class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashmap =defaultdict(int)
        i,j = 0,0,
        nums_len = len(nums)
        ans = 1
        
        # Sliding Window
        while i<nums_len and j < nums_len:
            hashmap[nums[j]] += 1
            while hashmap[nums[j]] > k:
                hashmap[nums[i]] -= 1
                i+=1
            if j-i+1 > ans:
                ans = j-i+1
            j+=1
        return ans
            
        