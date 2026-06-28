class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for k, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], k]
            else:
                d[n] = k