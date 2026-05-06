class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p = 0 
        min_pr = float('inf')

        for p in prices:

            min_pr = min(min_pr, p)

            max_p = max(max_p, p - min_pr)
        
        return max_p
        