class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = set()
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            canP = False
            canA = False
            visit = set()
            while q and (not canP or not canA):
                r,c = q.popleft()
                if (r,c) in ans:
                    return True
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr >=rows or nc>= cols:
                        canA = True
                    if nr<0 or nc <0:
                        canP = True
                    elif nr in range(rows) and nc in range(cols) and heights[nr][nc] <= heights[r][c] and (nr,nc) not in visit:
                        q.append((nr,nc))
                        visit.add((nr,nc))
            return canP and canA

                

        for r in range(rows):
            for c in range(cols):
                canFlow = bfs(r,c)
                if canFlow:
                    ans.add((r,c))
        return list(ans)
        