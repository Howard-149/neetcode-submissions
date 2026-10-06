class CountSquares:

    def __init__(self):
        self.points=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1,y1 = point[0],point[1]
        for diag_p, cnt in self.points.items():
            x2,y2 = diag_p
            if x1!=x2 and y1!=y2:
                ans += cnt*self.points.get((x1,y2),0)*self.points.get((x2,y1),0)
        return ans
            


