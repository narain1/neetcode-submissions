class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        stack = [([], candidates, 0)]
        res = []
        while stack:
            cur_nums, rem_nums, cur_sum = stack.pop()
            if cur_sum == target:
                res.append(cur_nums)
            elif cur_sum < target:
                for i in range(len(rem_nums)):
                    if i == 0 or rem_nums[i] != rem_nums[i - 1]:
                        stack.append((cur_nums + [rem_nums[i]],  rem_nums[i+1:], cur_sum + rem_nums[i]))
        return res