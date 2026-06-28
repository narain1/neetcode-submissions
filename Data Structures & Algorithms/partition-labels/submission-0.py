class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for k, c in enumerate(s):
            d[c] = k

        res = []
        size, end = 0, 0
        for k, c in enumerate(s):
            size += 1
            end = max(end, d[c])

            if k == end:
                res.append(size)
                size = 0
        return res