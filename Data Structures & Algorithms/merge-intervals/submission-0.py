class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])

        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])

            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged