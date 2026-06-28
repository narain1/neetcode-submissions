class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stack = [(0, 0), (1, 0)] # pos, cost
        min_cost = float("inf")

        while stack:
            pos, cur_cost  = stack.pop()
            if pos >= len(cost):
                min_cost = min(min_cost, cur_cost)
                continue
            stack.append((pos + 1, cur_cost + cost[pos]))
            stack.append((pos + 2, cur_cost + cost[pos]))
        return min_cost
        
            
