class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = zip(position,speed)
        pos_spd=sorted(pos_spd, key = lambda x: x[0], reverse=True)
        stack = []
        for p,s in pos_spd:
            time = (target-p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
