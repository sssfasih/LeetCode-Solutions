class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] = count[nums[i]]+1
            else:
                count[nums[i]] = 1
        heap = [(-value,key) for key,value in count.items()]
        heapify(heap)
    
        count = 0
        maxx = heappop(heap)[0]
        while heap and heappop(heap)[0] == maxx:
            count-=maxx
        return abs(count-maxx)

        