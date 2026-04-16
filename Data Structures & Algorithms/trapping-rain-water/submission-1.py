class Solution:
    def trap(self, height: List[int]) -> int:

        lx , rx = 0, len(height) - 1

        res = 0
        max_l = max_r = 0

        while lx < rx:

            if height[lx] < height[rx]:
                max_l = max(max_l, height[lx])
                res+= max_l - height[lx]
                lx+=1
            
            else:
                max_r = max(max_r, height[rx])
                res+= max_r - height[rx]
                rx-=1
        

        return res