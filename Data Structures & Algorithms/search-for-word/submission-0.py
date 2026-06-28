class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visiting = set() 
        def dfs(x, y, idx):
            if idx == len(word): return True
            if x < 0 or x >= m or y < 0 or y >= n or word[idx] != board[x][y] or (x, y) in visiting:
                return False

            visiting.add((x, y))
            result = (
                dfs(x + 1, y, idx + 1) or
                dfs(x - 1, y, idx + 1) or
                dfs(x, y + 1, idx + 1) or
                dfs(x, y - 1, idx + 1)
            ) 
            visiting.remove((x, y))

            return result

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False