class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        output = 0 
        for n in nums:
            output |= n
        return output << (len(nums) - 1)