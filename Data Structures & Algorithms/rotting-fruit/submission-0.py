class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        cnt = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    cnt+=1
        while q and cnt:
            l = len(q)
            for _ in range(l):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        cnt-=1
                        q.append((nr,nc))
            time+=1
        if cnt:
            return -1
        return time
        
