class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_ar = 0 

        lx, rx = 0 , len(heights) - 1

        while lx < rx:

            ar = min(heights[lx], heights[rx]) * (rx - lx)

            max_ar = max(max_ar, ar)

            if heights[lx] < heights[rx]:
                lx+=1
            
            else:
                rx-=1
        
        return max_ar

        