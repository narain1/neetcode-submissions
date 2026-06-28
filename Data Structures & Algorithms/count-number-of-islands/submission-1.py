class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(y, x):
            stack = [(y, x)]
            while stack:
                pos_y, pos_x = stack.pop()
                grid[pos_y][pos_x] = '0'
                for dy, dx in directions:
                    new_x, new_y = pos_x + dx, pos_y + dy
                    if 0<=new_y<m and 0<=new_x<n and grid[new_y][new_x] == '1':
                        stack.append((new_y, new_x))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count