class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1 :
            return ans
        
        def get_row(prev_row):
            temp =[1]
            for i in range(0,len(prev_row)-1):
                temp.append(prev_row[i]+prev_row[i+1])
            temp.append(1)
            return temp
        
        for i in range(1,numRows):
            ans.append(get_row(ans[i-1]))
            
        return ans
        