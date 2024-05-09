class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        hap_len = len(happiness)
        happiness.sort()
        max_hap = 0
        for i in range(k):
            if happiness[hap_len-i-1] -i > 0:
                max_hap += happiness[hap_len-i-1]-i
        return max_hap
        