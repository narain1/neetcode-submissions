class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # res = []

        # for i in range(1 << n):
        #     subset = [nums[j] for j in range(n) if (i & (1 << j))]
        #     res.append(subset)

        # return res

        # res = [[]]

        # for num in nums:
        #     res += [subset + [num] for subset in res]

        # return res

        res, subset = [], []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res