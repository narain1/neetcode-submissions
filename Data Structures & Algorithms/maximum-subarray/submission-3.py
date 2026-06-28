class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = nums[0]
        total = 0
        for n in nums:
            total += n
            output = max(total, output)
            if total < 0: total = 0
        return output