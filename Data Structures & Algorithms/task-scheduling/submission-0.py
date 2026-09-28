class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        cnts = Counter(tasks)
        queue = deque([(0,"idle")]*n)
        todo = 0
        for task, cnt in cnts.items():
            todo+=cnt
            heapq.heappush(max_heap,(-cnt,task))
        cycles = 0
        while todo:
            cycles+=1
            cnt,task = heapq.heappop(max_heap)
            if task!= "idle":
                todo -=1
            queue.append((cnt+1,task))
            reinsert = queue.popleft()
            if reinsert[0] < 0 or reinsert[1] == "idle":
                heapq.heappush(max_heap,reinsert)
        return cycles

