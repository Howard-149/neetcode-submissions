class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visit = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(r,c):
            q = deque()
            path = []
            surrounded = True
            visit.add((r,c))
            q.append((r,c))
            path.append((r,c))
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr not in range(rows) or nc not in range(cols):
                        surrounded = False
                    elif board[nr][nc] == "O" and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        q.append((nr,nc))
                        path.append((nr,nc))
            if surrounded:
                for r,c in path:
                    board[r][c] = "X"
            return
                

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visit:
                    bfs(r,c)
        return 