class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        answer = [[[]for x in range(len(grid)-2)] for _ in range(len(grid)-2)]
        
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                answer[i][j] = max(grid[i][j],grid[i+1][j],grid[i+2][j],grid[i][j+1],grid[i][j+2],grid[i+1][j+1],grid[i+1][j+2],grid[i+2][j+1],grid[i+2][j+2])
        return answer 
        