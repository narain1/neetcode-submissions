class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rev_map = {'}': '{', ']': '[', ')': '('}
        for c in s:
            if c in rev_map:
                if stack and stack[-1] == rev_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
