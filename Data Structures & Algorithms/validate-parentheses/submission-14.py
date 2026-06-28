class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        rev_d = {v:k for k, v in d.items()}
        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            elif c in d.values() and stack and stack[-1] == rev_d[c]:
                stack.pop()
            else:
                return False
        return not stack
