class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lx , rx = 0 , 1 
        max_p = 0

        while rx < len(prices):

            if prices[lx] < prices[rx]:
                profit = prices[rx] - prices[lx]
                max_p = max(profit,max_p)
            
            else:
                lx = rx

            rx+=1
        
        return max_p



        