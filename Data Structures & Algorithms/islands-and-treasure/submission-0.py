class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            distance = 1
            while q:
                l = len(q)
                for _ in range(l):
                    r,c = q.popleft()
                    for dr,dc in directions:
                        new_r, new_c = r+dr,c+dc
                        if new_r in range(rows) and new_c in range(cols) and distance < grid[new_r][new_c]:
                            grid[new_r][new_c] = distance
                            q.append((new_r,new_c))
                distance+=1
            return
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs(r,c)
        return 