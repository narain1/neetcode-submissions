class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    grid[i][j] = 0
                    area = 1
                    while stack:
                        xx, yy = stack.pop()
                        for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                            nx, ny = xx + dx, yy + dy
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1: 
                                stack.append((nx, ny))
                                grid[nx][ny] = 0
                                area += 1
                        max_area = max(area, max_area)
        return max_area
                    
                            