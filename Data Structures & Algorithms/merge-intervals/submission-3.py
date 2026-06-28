class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)
        output = [intervals[0]]

        for start, end in intervals:
            lastend = output[-1][1]
            if start <= lastend:
                output[-1][1] = max(lastend, end)
            else:
                output.append([start, end])
        return output
