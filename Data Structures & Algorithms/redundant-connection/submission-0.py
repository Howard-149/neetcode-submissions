class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return 0
            elif rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        for a,b in edges:
            n1,n2 = a-1,b-1 
            if not union(n1,n2):
                return [a,b]
        return ans