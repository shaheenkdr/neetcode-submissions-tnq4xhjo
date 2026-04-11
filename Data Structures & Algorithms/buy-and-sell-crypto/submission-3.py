class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_p, max_p = 102, 0

        for price in prices:

            min_p = min(min_p, price)

            max_p = max(max_p, price - min_p)
        
        return max_p

        
        