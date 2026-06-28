class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in m:
                return [m[diff], idx]
            m[n] = idx