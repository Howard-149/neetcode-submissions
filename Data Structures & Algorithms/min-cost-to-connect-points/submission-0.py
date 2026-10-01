class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(n):
                x1, y1 = points[i]
                if j != i:
                    x2, y2 = points[j]
                    dis = abs(x2-x1) + abs(y2-y1)
                    edges[i].append((dis,j))
        minheap = edges[0]
        heapq.heapify(minheap)
        visit = set([0])
        ans = 0
        while minheap and len(visit) != n:
            cost, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            ans += cost
            for cost2, n2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap,(cost2, n2))
        return ans