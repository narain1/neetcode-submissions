class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = [1] * n

        left = 1
        for k, c in enumerate(nums):
            a[k] = left
            left *= c

        right = 1
        for i in range(len(nums)-1, -1, -1):
            a[i] *= right
            right *= nums[i]
        
        return a
        