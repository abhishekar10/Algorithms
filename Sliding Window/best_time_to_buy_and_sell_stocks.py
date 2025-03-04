class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,profit = 0,1,0
        while r < len(prices):
            if prices[l] < prices[r] :
                temp = prices[r] - prices[l]
                profit = max(temp,profit)
            else :
                l = r
            r += 1
        return profit