class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] # [temp, indices]
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                stemp, sindex = stack.pop()
                res[sindex] = i - sindex

            stack.append([temp, i]) 
        
        return res

        