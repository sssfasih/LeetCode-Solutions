class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        arr=[[]]
        for i in range(len(nums)):
            for j in range(len(arr)):
                if nums[i] in arr[j]:
                    if j >= len(arr)-1:
                        arr.append([nums[i]])
                    else:continue
                else:
                    arr[j].append(nums[i])
                    break
        return arr
                    
        