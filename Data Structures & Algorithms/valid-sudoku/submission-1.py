class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rs, cs, bs = defaultdict(list), defaultdict(list), defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                if board[i][j] in rs[i] or board[i][j] in cs[j] or board[i][j] in bs[(i//3, j//3)]:
                    return False
                else:
                    rs[i].append(board[i][j])
                    cs[j].append(board[i][j])
                    bs[(i//3, j//3)].append(board[i][j])
        return True
