class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        stack = [([], nums)]
        while stack:
            perm, remaining_nums = stack.pop()
            if len(perm) == len(nums):
                output.append(perm)
            for idx in range(len(remaining_nums)):
                stack.append((perm + [remaining_nums[idx]], remaining_nums[:idx] + remaining_nums[idx+1:]))
        return output