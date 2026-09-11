class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = [[0]*9 for _ in range(9)]
        col_seen = [[0]*9 for _ in range(9)]
        block_seen = [[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                data = board[i][j]
                if data!=".":
                    num = ord(data) - ord("1")
                    block = i//3*3 + j//3
                    if row_seen[i][num] !=0:
                        return False
                    if col_seen[j][num] !=0:
                        return False
                    if block_seen[block][num]!=0:
                        return False
                    row_seen[i][num]+=1
                    col_seen[j][num]+=1
                    block_seen[block][num]+=1

        return True