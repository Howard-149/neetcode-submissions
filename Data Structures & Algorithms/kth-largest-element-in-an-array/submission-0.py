class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap)>=k:
                heapq.heappushpop(heap,n)
            else:
                heapq.heappush(heap,n)
        return heapq.heappop(heap)