class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            dis = math.sqrt(p[0]**2+p[1]**2)
            if len(heap)>=k:
                heapq.heappushpop(heap,(-dis,p))
            else:
                heapq.heappush(heap,(-dis,p))
        ans = [ item[1] for item in heap]
        return ans