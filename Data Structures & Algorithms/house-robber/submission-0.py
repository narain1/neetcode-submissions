class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        last_2, last_1 = 0, nums[0]
        res = 0
        for i in range(1, len(nums)):
            current = max(last_1, last_2 + nums[i])
            last_2 = last_1
            last_1 = current
        return last_1
       
        # prev2, prev1 = 0, nums[0]
        # for i in range(1, len(nums)):
        #     current = max(prev1, prev2 + nums[i])
        #     prev2 = prev1
        #     prev1 = current
        # return prev1
