class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rev_map = {'}': '{', ']':'[', ')': '('}
        for i in range(len(s)):
            c = s[i]
            if c in '([{':
                stack.append(c)
            elif c in ')]}' and stack and rev_map[c] == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack