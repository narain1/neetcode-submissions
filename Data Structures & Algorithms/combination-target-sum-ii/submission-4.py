class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        candidates.sort()

        def dfs(idx, comb, sum):
            if sum == target:
                result.add(tuple(comb))
                return
            
            if idx == len(candidates) or sum > target:
                return

            comb.append(candidates[idx])
            dfs(idx + 1, comb, sum + candidates[idx])
            comb.pop()

            while idx + 1 < len(candidates) and candidates[idx + 1] == candidates[idx]:
                idx += 1
            
            dfs(idx + 1, comb, sum)

        dfs(0, [], 0)
        return list(map(list, result)) 