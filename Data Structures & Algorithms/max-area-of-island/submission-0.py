class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # df
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.max_area = 0
        h, w = len(grid), len(grid[0])

        def dfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0
            area = 1

            while q:
                i, j = q.popleft()
                for d in directions:
                    i1, j1 = i + d[0], j + d[1]
                    if  i1 >= 0 and j1 >= 0 and j1 < w and i1 < h and grid[i1][j1] == 1:
                        area += 1
                        q.append((i1, j1))
                        grid[i1][j1] = 0

            self.max_area = max(area, self.max_area)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
        
        return self.max_area

