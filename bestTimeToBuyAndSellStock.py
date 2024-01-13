# Key idea
# Initialize the first element as the minimum price and keep track of the minimum price at each iteration of the loop. Keep track of the max profit by subtracting the current
# price by our minimum price.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMaxProfit = 0
        currMin = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]
            if prices[i] - currMin > currMaxProfit:
                currMaxProfit = prices[i] - currMin
        return currMaxProfit
