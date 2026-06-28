class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for crs, pre in prerequisites:
            d[crs].append(pre)

        visiting = set()

        def has_cycle(crs):
            if crs in visiting: return False

            if d[crs] == []: return True

            visiting.add(crs)
            for pre in d[crs]:
                if not has_cycle(pre):
                    return False

            visiting.remove(crs)
            d[crs] = []
            return True

        for crs in range(numCourses):
            if not has_cycle(crs):
                return False

        return True