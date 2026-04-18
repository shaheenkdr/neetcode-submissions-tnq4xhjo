class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] # [index, height]
        
        max_ar = 0

        for i, h in enumerate(heights + [0]):
            
            start = i 

            while stack and stack[-1][1] > h:

                s_index , s_height = stack.pop()

                max_ar = max(max_ar, s_height * (i - s_index))
                
                start = s_index
            
            stack.append([start, h])
        
        return max_ar



        