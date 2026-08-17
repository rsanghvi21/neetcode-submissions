class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for i in range(len(prices) - 1, -1, -1):
            index = 0
            while index < i:
                profit = prices[i] - prices[index]
                if profit >= maxProf:
                    maxProf = profit
                index += 1
        return maxProf
        