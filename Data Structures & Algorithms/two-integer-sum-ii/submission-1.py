class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lx, rx = 0, len(numbers) - 1 


        while lx < rx: 

            res = numbers[lx] + numbers[rx]

            if res == target:
                return [lx+1, rx+1]
            
            elif res < target:
                lx+=1
            else:
                rx-=1
        