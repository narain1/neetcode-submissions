class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = [([], 0, 0)]
        while stack:
            subset, cur_sum, idx = stack.pop()
            if cur_sum == target:
                res.append(subset.copy())
                continue
            
            for i in range(idx, len(nums)):
                if cur_sum + nums[i] <= target:
                    new_subset = subset  + [nums[i]]
                    stack.append((new_subset, cur_sum + nums[i], i))
        return res
                
        
        