class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sofar = prices[0]
        max_prof = 0

        for i in range(1,len(prices)):
            max_prof = max(max_prof, prices[i] - min_sofar)
            min_sofar = min(min_sofar, prices[i])

        return max_prof




        