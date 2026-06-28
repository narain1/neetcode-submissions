class Solution:
    def checkValidString(self, s: str) -> bool:
        stack, stars = [], []
        for idx, ch in enumerate(s):
            if ch == "(": stack.append(idx)
            elif ch == "*": stars.append(idx)
            else:
                if not stack and not stars:
                    return False
                if stack: stack.pop()
                else: stars.pop()
        
        while stack and stars:
            if stack.pop() > stars.pop():
                return False
        return not stack