class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        s = 0
        for a,b in zip(gas,cost):
            diff.append(a-b)
            s+=a-b
        if s<0:
            return -1
        start_idx = 0
        cur_s = 0
        for i in range(len(diff)):
            cur_s += diff[i]
            if cur_s<0:
                cur_s = 0
                start_idx = i+1
        return start_idx%len(diff)

        