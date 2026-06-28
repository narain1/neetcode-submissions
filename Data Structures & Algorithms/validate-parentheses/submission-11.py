class Solution:
    def isValid(self, s: str) -> bool:
        rev_map = {"}": "{", "]": "[", ")": "("}
        stack = []
        for c in s:
            if len(stack) > 0 and c in rev_map and stack[-1] == rev_map[c]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
