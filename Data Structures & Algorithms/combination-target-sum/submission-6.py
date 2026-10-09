class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(idx, cur, sum):
            if sum == target:
                result.append(cur.copy())
                return

            if idx == len(nums) or sum > target:
                return 
            
            cur.append(nums[idx])
            dfs(idx, cur, sum + nums[idx])
            cur.pop()
            dfs(idx + 1, cur, sum)
        

        dfs(0, [], 0) # idx, comb, sum
        return result