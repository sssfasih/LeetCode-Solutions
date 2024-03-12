class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minn = 999
        arr.sort()
        out = []
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                if arr[i+1]-arr[i] == minn:
                    out.append([arr[i],arr[i+1]])
                elif arr[i+1]-arr[i] < minn:
                    minn = arr[i+1]-arr[i]
                    out=[[arr[i],arr[i+1]]]
        return out