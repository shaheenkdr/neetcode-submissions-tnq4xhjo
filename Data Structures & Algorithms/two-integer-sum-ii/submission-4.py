class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lx, rx = 0 , len(numbers) - 1

        while lx < rx:

            val = numbers[lx] + numbers[rx]

            if val == target:
                return [lx+1, rx+1]
            
            elif val > target:
                rx-=1
            
            else:
                lx+=1
                
        