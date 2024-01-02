class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        for loop in range(len(self.matrix[0])):
            if loop > 0:
                print(self.matrix[0][loop])
                print(self.matrix[0][loop-1])
                self.matrix[0][loop] += self.matrix[0][loop-1]
                print(self.matrix[0][loop])
        
        for loop in range(len(self.matrix)):
            if loop > 0:
                self.matrix[loop][0] += self.matrix[loop-1][0]
                
        for i in range(1,len(self.matrix)):
            for j in range(1,len(self.matrix[i])):
                self.matrix[i][j] += self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    
        if (row1==0 and col1==0):
            x = self.matrix[row2][col2]
        elif row1==0:
            x = self.matrix[row2][col2]-self.matrix[row2][col1-1]
        elif col1==0:
            x = self.matrix[row2][col2]-self.matrix[row1-1][col2]
            
        else:
            x = self.matrix[row2][col2]-self.matrix[row1-1][col2]-self.matrix[row2][col1-1] +self.matrix[row1-1][col1-1]
        
        return x
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)