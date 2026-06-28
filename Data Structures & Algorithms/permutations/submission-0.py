class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = [([], nums)]
        output = []

        while stack:
            cur_perm, rem = stack.pop()
            if not rem:
                output.append(cur_perm)
                continue
            
            for i in range(len(rem)):
                new_perm = cur_perm + [rem[i]]
                new_rem = rem[:i] + rem[i + 1:]
                stack.append((new_perm, new_rem))
        return output