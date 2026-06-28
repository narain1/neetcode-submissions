class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(cur, total, pos):
            if total == target:
                res.append(cur.copy())
                return
            if pos >= len(nums) or total > target:
                return

            cur.append(nums[pos])
            dfs(cur, total + nums[pos], pos)
            cur.pop()
            dfs(cur, total, pos + 1)

        dfs([], 0, 0)
        return res