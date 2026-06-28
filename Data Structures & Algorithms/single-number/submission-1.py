class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = sum(nums)
        b = sum(set(nums))
        x = 2*b - a
        return x