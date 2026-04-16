class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] # [temp, index]
        res = [0] * len(temperatures)

        for i, val in enumerate(temperatures):

            while stack and stack[-1][0] < val:

                stemp, sindex = stack.pop()

                res[sindex] = i - sindex
            
            stack.append([val, i])
        

        return res
        