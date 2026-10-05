class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_r = [False] * m
        zero_c = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_r[i] = True
                    zero_c[j] = True
        for i in range(m):
            for j in range(n):
                if zero_r[i] or zero_c[j]:
                    matrix[i][j] = 0
        return
                
        