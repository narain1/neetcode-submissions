class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for course, pre in prerequisites:
            d[course].append(pre)

        visiting, visited = set(), set()
        output = []

        def dfs(course):
            if course in visiting: return False
            if course in visited: return True

            visiting.add(course)

            for c in d[course]:
                if not dfs(c):
                    return False

            visiting.remove(course)
            visited.add(course)
            output.append(course)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output