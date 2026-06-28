class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        stack = [(0, 0)]
        while stack:
            cur_sum, idx = stack.pop()
            if idx == len(nums):
                if cur_sum == target:
                    count += 1
                continue

            stack.append((cur_sum - nums[idx], idx + 1))
            stack.append((cur_sum + nums[idx], idx + 1))
        return count
        