class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = Counter(tasks)
        max_heap = [-c for t,c in cnts.items()]
        heapq.heapify(max_heap)
        queue = deque([])
        todo = 0
        cycles = 0
        while max_heap or queue:
            cycles+=1
            if max_heap:
                cnt = heapq.heappop(max_heap)
                if cnt<-1:
                    queue.append((cnt+1,cycles+n))
            if queue:
                if queue[0][1] == cycles:
                    reinsert = queue.popleft()
                    heapq.heappush(max_heap,reinsert[0])
        return cycles

