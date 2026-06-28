class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        stack = [(0, 0)]
        while stack:
            x_pos, y_pos = stack.pop()
            if x_pos == m- 1 and y_pos == n - 1:
                count += 1
                continue
            if x_pos > m: continue
            if y_pos > n: continue
            stack.append((x_pos + 1, y_pos))
            stack.append((x_pos, y_pos + 1))
        return count
        