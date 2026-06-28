"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        sorted_intervals = [i for j in sorted_intervals for i in (j.start, j.end)]
        return all(x <= y for x, y in zip(sorted_intervals, sorted_intervals[1:]))
