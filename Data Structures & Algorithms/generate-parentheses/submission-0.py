class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack = []
        # res = []
        # def backtrack(open_n, closed_n):
        #     if open_n == closed_n == n:
        #         res.append("".join(stack))
        #         return
            
        #     if open_n < n:
        #         stack.append('(')
        #         backtrack(open_n + 1, closed_n)
        #         stack.pop()
        #     if closed_n < open_n:
        #         stack.append(')')
        #         backtrack(open_n, closed_n + 1)
        #         stack.pop()
        # backtrack(0, 0)
        # return res
        result = []
        stack = [("", 0, 0)]  # (current_string, open_count, close_count)
        
        while stack:
            curr_string, open_count, close_count = stack.pop()
            
            # If both open and close counts equal n, we have a valid combination
            if open_count == n and close_count == n:
                result.append(curr_string)
                continue
            
            # Option 1: Add an opening parenthesis if we haven't used n yet
            if open_count < n:
                stack.append((curr_string + "(", open_count + 1, close_count))
            
            # Option 2: Add a closing parenthesis if we have an unmatched open
            if close_count < open_count:
                stack.append((curr_string + ")", open_count, close_count + 1))
        
        return result