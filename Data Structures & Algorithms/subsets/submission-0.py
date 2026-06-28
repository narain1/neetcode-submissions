class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        return [list(j) for i in range(len(nums)+1) for j in combinations(nums, i)]