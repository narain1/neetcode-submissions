class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    grid[i][j] = 0
                    area = 1

                    while stack:
                        x, y = stack.pop()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                                area += 1
                                grid[nx][ny] = 0
                                stack.append((nx, ny))
                        
                        max_area = max(max_area, area)
        return max_area

