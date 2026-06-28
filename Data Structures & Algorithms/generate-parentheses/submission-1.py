class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [('', 0, 0)]
        result = []
        while stack:
            cur_str, open_n, close_n = stack.pop()
            if close_n == n and open_n == n:
                result.append(cur_str)
            if open_n < n:
                stack.append((cur_str + '(', open_n + 1, close_n))
            if close_n < open_n:
                stack.append((cur_str + ')', open_n, close_n + 1))
        return result