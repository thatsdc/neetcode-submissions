class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_v = 0
        max_v = 0
        temp_min = 1000
        temp_max = 0

        for i in range(len(prices)):
            p = prices[i]
            if p < temp_min:
                temp_min = p
                temp_max = 0

            if p > temp_max:
                temp_max = p
            
            if temp_max - temp_min > max_v - min_v: 
                min_v = temp_min
                max_v = temp_max

        
        return max_v - min_v
