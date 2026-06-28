class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 0

        for num in nums:
            it = 1
            while (num + 1) in store:
                it += 1
                num += 1
            longest = max(longest, it)
        return longest