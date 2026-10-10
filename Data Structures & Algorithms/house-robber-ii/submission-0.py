class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def rob_linear(houses):
            n = len(houses)
            dp = [0] * (n + 1)
            dp[1] = houses[0]

            for i in range(2, n + 1):
                dp[i] = max(
                    dp[i - 1], # no pick
                    dp[i - 2] + houses[i - 1] # pick
                )

            return dp[n]

        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )