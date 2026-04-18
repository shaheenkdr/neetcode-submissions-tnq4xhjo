class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        fleet = [[p,s] for p,s in zip(position,speed)]

        fcount = prev = 0 


        for p,s in sorted(fleet, reverse=True):

            time = (target - p) / s

            if time > prev: 
                fcount+=1 
                prev = time
        
        return fcount

