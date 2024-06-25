class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ans = defaultdict(int)
        count = [[] for i in range(len(nums))]
        counter = 0
        answer = []
        for i in range(len(nums)):
            ans[nums[i]] += 1

        for i,j in ans.items():
            count[j-1].append(i)
        
        print(count)
        for i in range(len(count)-1,-1,-1):
            for j in range(len(count[i])):
                if counter ==k:
                    return answer
                answer.append(count[i][j])
                counter += 1
        return answer