class myque:
    def __init__(self):
        self.queue = deque()
    def pop(self,value):
        if self.queue and self.front() == value:
            self.queue.popleft()
    def push(self,value):
        while self.queue and value> self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    def front(self):
        return self.queue[0]
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_queue = myque()
        ans = []
        for i in range(k):
            max_queue.push(nums[i])
        ans.append(max_queue.front())
        for i in range(k,len(nums)):
            max_queue.pop(nums[i-k])
            max_queue.push(nums[i])
            ans.append(max_queue.front())
        return ans

        