class Solution:
    def trap(self, height: List[int]) -> int:

        lx, rx = 0, len(height) - 1

        lmax = rmax = -1

        res = 0

        while lx < rx:

            if height[lx] < height[rx]:
                lmax = max(lmax, height[lx])
                res += lmax - height[lx]
                lx+=1
            
            else:
                rmax = max(rmax, height[rx])
                res+= rmax - height[rx]
                rx-=1
        
        return res
        