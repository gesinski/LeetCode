class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            if prices[min_buy] < prices[sell]:
                profit = prices[sell] - prices[min_buy]
                max_profit = max(max_profit, profit)
            else:
                min_buy = sell
            sell += 1
        
        return max_profit