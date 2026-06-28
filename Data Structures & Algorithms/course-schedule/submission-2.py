class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for crs, pre in prerequisites:
            d[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited: return False

            if d[crs] == []: return True

            visited.add(crs)
            for pre in d[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            d[crs] = []
            return True



        for idx in range(numCourses):
            if not dfs(idx):
                return False
        
        return True
        