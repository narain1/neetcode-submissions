class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_prereq_map = defaultdict(list)
        for crs, pre in prerequisites:
            course_prereq_map[crs].append(pre)

        visiting = set()
        def has_cycle(crs):
            if crs in visiting: return False
            if course_prereq_map[crs] == []:
                return True

            visiting.add(crs)
            for pre in course_prereq_map[crs]:
                if not has_cycle(pre):
                    return False
            visiting.remove(crs)
            course_prereq_map[crs] = []
            return True

        for crs in range(numCourses):
            if not has_cycle(crs):
                return False
        
        return True