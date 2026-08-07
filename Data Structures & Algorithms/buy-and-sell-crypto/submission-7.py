class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices: 
            return 0

        min_p = 1000
        profit = 0
        for p in prices:
            if p < min_p:
                min_p = p

            if p - min_p > profit:
                profit = p - min_p

        return profit

