class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        stack = [([], 0)]
        while stack:
            cur_subset, idx = stack.pop()
            if idx == len(nums):
                output.append(cur_subset)
                continue

            stack.append((cur_subset, idx + 1))
            stack.append((cur_subset + [nums[idx]], idx + 1))
        return output