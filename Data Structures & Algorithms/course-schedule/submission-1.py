class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[pre].append(course)

        visiting = set()
        done = set()

        def dfs(course):

            # cycle
            if course in visiting:
                return False

            # already completely checked
            if course in done:
                return True

            visiting.add(course)

            for nxt in graph[course]:
                if not dfs(nxt):
                    return False

            visiting.remove(course)
            done.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True