class Solution:
    def maxArea(self, heights: List[int]) -> int:

        lx , rx = 0 , len(heights) - 1

        max_ar = 0 


        while lx < rx: 

            area = abs(lx-rx) * min(heights[lx], heights[rx])

            max_ar = max(max_ar, area)

            if heights[lx] < heights[rx]:
                lx+=1
            else:
                rx-=1
            

        return max_ar
        