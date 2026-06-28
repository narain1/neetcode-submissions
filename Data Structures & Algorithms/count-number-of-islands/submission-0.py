class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        R, C = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c):
            if (r<0 or c<0 or r>=R or c>=C or grid[r][c] == '0'):
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr, c+dc)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
        return res