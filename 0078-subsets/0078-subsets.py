class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []
        # Backtracking
        def dfs(i):
            # Leave Node
            if i >= len(nums):
                subsets.append(subset.copy())
                return
            
            # Adding condition 
            subset.append(nums[i])
            dfs(i+1)
            
            # Non Adding condition
            subset.pop()
            dfs(i+1)
                
        dfs(0)    
        return subsets