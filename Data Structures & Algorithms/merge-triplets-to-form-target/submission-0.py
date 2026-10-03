class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur_a,cur_b, cur_c = 0,0,0
        ta,tb,tc = target
        print(ta,tb,tc)
        for a,b ,c in triplets:
            if a<= ta and b<= tb and c<= tc:
                cur_a, cur_b, cur_c = max(a,cur_a), max(b,cur_b), max(c, cur_c)
        return (cur_a,cur_b, cur_c) == (ta,tb,tc)
                
