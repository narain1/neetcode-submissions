class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(': ')', '{': '}', '[': ']'}
        rev_d = {j:i for i,j in d.items()}
        
        for c in s:
            if c in d:
                stack.append(c)
            elif c in rev_d and stack and stack[-1] == rev_d[c]:
                stack.pop()
            else:
                return False
        return not stack