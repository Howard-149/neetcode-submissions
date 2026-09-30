class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)
        visiting = set()
        visited = set()
        ans = []
        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True
            visiting.add(c)
            for p in prereq[c]:
                if not dfs(p):
                    return False
            visiting.remove(c)
            visited.add(c)
            ans.append(c)
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans