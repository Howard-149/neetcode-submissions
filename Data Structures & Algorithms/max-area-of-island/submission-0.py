class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        visit = set()
        rows, cols = len(grid),len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            area = 1
            while q:
                cur_r, cur_c = q.popleft()
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr,dc in directions:
                    r,c = cur_r+dr, cur_c+dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c] == 1:
                        q.append((r,c))
                        visit.add((r,c))
                        area+=1
            return area
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:
                    area = bfs(i,j)
                    max_area = max(area,max_area)
        return max_area