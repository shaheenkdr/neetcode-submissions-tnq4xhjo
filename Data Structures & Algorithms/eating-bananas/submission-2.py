class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lx, rx = 1, max(piles)
        res = float("inf")

        while lx <= rx: 

            k = (rx + lx) // 2 # <- mid basically

            hours = 0

            for p in piles:
                hours+= math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                rx = k - 1
            
            else:
                lx = k + 1

        return res 


        