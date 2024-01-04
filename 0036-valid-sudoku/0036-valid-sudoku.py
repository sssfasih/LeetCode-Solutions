class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        moves = []
        
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    moves += [(i, element), (element, j), (i // 3, j // 3, element)]
                    
        return len(moves) == len(set(moves))
        