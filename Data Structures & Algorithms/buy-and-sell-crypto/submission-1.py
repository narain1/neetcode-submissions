class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1                                     # 2 pointers for the first two elements booth pointers need not be in the same 0,1 are good starting point
        maxp = 0                                        # element for maxprofit

        while r < len(prices):                          # until right pointer is less than the length of the prices list
            if prices[l] < prices[r]:                   # calcualte the profit for the left and right pointers
                profit = prices[r] - prices[l]          # update the maximum profit 
                maxp = max(profit, maxp)
            else:                                       #if right pointer is less than left pointer then the value is decreasing we can skip that segment hence move left pointer in place of right pointer
                l = r                                   
            r += 1                                      # move right pointer one away from left pointer
        return maxp