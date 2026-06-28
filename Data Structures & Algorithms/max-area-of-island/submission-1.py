class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        max_area = 0

        def dfs(y, x):
            stack = [(y, x)]
            area = 0
            grid[y][x] = 0
            while stack:
                xi, xj = stack.pop()
                area += 1
                for dy, dx in directions:
                    new_y, new_x = xi + dy, xj + dx
                    if 0<=new_y<m and 0<=new_x< n and grid[new_y][new_x] == 1:
                        stack.append((new_y, new_x))
                        grid[new_y][new_x] = 0
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)  
                    max_area = max(area, max_area)
        return max_area

        