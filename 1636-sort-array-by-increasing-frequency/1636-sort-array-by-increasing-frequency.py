class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq=collections.Counter(nums)
        val=sorted(set(freq.values()))
        res=[]
        for i in val:
            ans=[]
            for j in freq:
                if freq[j]==i:
                    for k in range(i):
                        ans.append(j)
            if len(set(ans))>1:
                ans.sort(reverse=True)
            for i in ans:
                res.append(i)
        return res