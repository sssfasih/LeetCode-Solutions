class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        values = list(counter.values())
        count = 0
        
        values.sort()
        
        for i in range(len(values)):
            if k > values[i]:
                k -= values[i]
                values[i] = 0
            else:
                values[i] -= k
                k = 0
            if values[i] != 0:
                count += 1
                
        return count