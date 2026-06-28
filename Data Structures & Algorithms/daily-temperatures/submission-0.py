class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n = len(temperatures)
        # res = []

        # for i, t in enumerate(temperatures):
        #     j = i + 1
        #     while j < n:
        #         if temperatures[j] > temperatures[i]:
        #             break
        #         j += 1
        #     count = 0 if j == n else j - i
        #     res.append(count)
        # return res

        n = len(temperatures)
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
            stack.append((t, i))
        return res
        