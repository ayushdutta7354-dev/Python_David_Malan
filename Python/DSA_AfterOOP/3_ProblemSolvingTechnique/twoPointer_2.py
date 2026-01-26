# Buy sell stock using two pointer:


class BuySellStock:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        minPrice = prices[0]
        ans = 0

        for i in range(n):
            current_profit = prices[i] - minPrice
            ans = max(current_profit, ans)
            minPrice = min(prices[i], minPrice)

        return ans
    

day_1 = BuySellStock();

print(day_1.maxProfit([45,3,8,6,88,95,86,100]));