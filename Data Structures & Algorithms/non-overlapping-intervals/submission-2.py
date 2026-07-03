class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        count = 0
        ptr = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= ptr:
                ptr = end
            else:
                count += 1
                ptr = min(ptr, end)

        return count