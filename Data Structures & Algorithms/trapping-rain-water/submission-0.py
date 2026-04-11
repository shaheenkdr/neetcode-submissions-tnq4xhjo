class Solution:
    def trap(self, height: List[int]) -> int:
        
        lx, rx = 0, len(height) - 1

        left_max, right_max = height[lx], height[rx]

        res = 0

        while lx < rx: 

            if height[lx] < height[rx]:
                lx+=1
                left_max = max(left_max, height[lx])
                res += left_max - height[lx]
            
            else:
                rx-=1
                right_max = max(right_max, height[rx])
                res+= right_max - height[rx]
            
        
        return res
