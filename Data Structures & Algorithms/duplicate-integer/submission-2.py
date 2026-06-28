class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for a in nums:
            if a in d:
                return True
            d[a] = 1
        return False
