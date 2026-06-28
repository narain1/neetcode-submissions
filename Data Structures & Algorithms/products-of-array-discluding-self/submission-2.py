class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = [1] * n

        l = 1
        for i in range(n):
            a[i] *= l
            l *= nums[i]

        r = 1
        for i in range(n -1, -1, -1):
            a[i] *= r
            r *= nums[i]
        return a
        