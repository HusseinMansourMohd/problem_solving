#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price and the maximum profit
        min_price = float('inf')
        max_profit = 0
        
        # Iterate through the prices and update the minimum price and the maximum profit
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        # Return the maximum profit
        return max_profit