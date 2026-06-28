class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0: return -1
        if amount == 0: return 0

        q = deque([(0, 0)]) # cur_sum, n_coins
        min_coins = float("inf")
        visited = set([0])

        while q:
            cur_sum, n_coins = q.popleft()
            for coin in coins:
                new_amount = cur_sum + coin
                if new_amount == amount:
                    min_coins = min(n_coins + 1, min_coins)
                if new_amount < amount and new_amount not in visited:
                    visited.add(new_amount)
                    q.append((new_amount, n_coins + 1))
        return min_coins if min_coins != float("inf") else -1

        # if amount == 0:
        #     return 0
        # if not coins:
        #     return -1
        
        # queue = deque([(0, 0)])  # (current_amount, num_coins)
        # visited = set([0])       # Track visited amounts
        # min_count = float("inf")
        
        # while queue:
        #     curr_amount, num_coins = queue.popleft()
            
        #     for coin in coins:
        #         next_amount = curr_amount + coin
        #         if next_amount == amount:
        #             min_count = min(min_count, num_coins + 1)
        #         elif next_amount < amount and next_amount not in visited:
        #             visited.add(next_amount)
        #             queue.append((next_amount, num_coins + 1))
        
        # return min_count if min_count != float("inf") else -1