class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = [[0]*9 for _ in range(9)]
        col_seen = [[0]*9 for _ in range(9)]
        block_seen = [[0]*9 for _ in range(9)]  
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    block = 3*(i//3) + j//3
                    digit = ord(board[i][j]) - ord("0")-1
                    if row_seen[i][digit] or col_seen[j][digit]  or block_seen[block][digit]:
                        return False
                    row_seen[i][digit] = True
                    col_seen[j][digit] = True
                    block_seen[block][digit] = True
        return True