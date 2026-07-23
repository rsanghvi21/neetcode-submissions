class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        # Check Rows
        for i in range(0, 9):
            s = set()
            for j in range(0, 9):
                if board[i][j] != '.':
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
        # Check Columns
        for i in range(0, 9):
            s = set()
            for j in range(0, 9):
                if board[j][i] != '.':
                    if board[j][i] in s:
                        return False
                    s.add(board[j][i])
        # Check boxes
        box = {}
        for i in range(0, 9):
            for j in range(0, 9):
                coord = (i // 3, j // 3)
                if coord not in box:
                    box[coord] = set()
                if board[i][j] != '.':  
                    if board[i][j] in box[coord]:
                        return False
                    box[coord].add(board[i][j])
        return True
            