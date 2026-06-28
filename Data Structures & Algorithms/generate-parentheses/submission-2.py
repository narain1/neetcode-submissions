class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [('', 0, 0)]
        output = []
        while stack:
            cur_str, open_n, close_n = stack.pop()
            if open_n == n and close_n == n:
                output.append(cur_str)
            if open_n < n:
                stack.append((cur_str + '(', open_n + 1, close_n))
            if close_n < open_n:
                stack.append((cur_str + ')', open_n, close_n + 1))
        return output 