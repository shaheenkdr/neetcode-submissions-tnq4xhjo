class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p = 0

        min_pr = float("inf")

        for num in prices: 

            min_pr = min(min_pr, num)

            max_p = max(max_p, num - min_pr)
        
        return max_p
        