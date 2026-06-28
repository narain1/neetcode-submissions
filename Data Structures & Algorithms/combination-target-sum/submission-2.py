class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        stack = [([], 0, 0)]
        while stack:
            subset, cur_sum, idx = stack.pop()
            if cur_sum == target:
                output.append(subset.copy())
                continue
            if idx < len(nums):
                if cur_sum + nums[idx] <= target:
                    stack.append((subset + [nums[idx]], cur_sum + nums[idx], idx))
                stack.append((subset, cur_sum, idx + 1))
        return output
