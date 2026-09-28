class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        heapq.heapify(maxheap)
        for s in stones:
            heapq.heappush(maxheap,-s)
        while len(maxheap)>1:
            x = -1*heapq.heappop(maxheap)
            y = -1*heapq.heappop(maxheap)
            if x-y != 0:
                heapq.heappush(maxheap,(y-x))
        if not maxheap:
            return 0
        else:
            return abs(maxheap[0])