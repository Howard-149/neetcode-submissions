class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.timemap[key]
        l = 0
        r = len(lst)-1
        target = timestamp
        while l<=r:
            mid = (l+r)//2
            if lst[mid][0] == target:
                return lst[mid][1]
            elif lst[mid][0] > target:
                r = mid-1
            else:
                l = mid+1
        if r<0:
            return ""
        else:
            return lst[r][1]
