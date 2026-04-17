class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        pairs =[ [p,s] for p,s in zip(position, speed)]

        prev_time = fleet = 0


        for p,s in sorted(pairs, reverse = True):

            time = (target - p) / s

            if time > prev_time:
                fleet+=1
                prev_time = time

            
        
        return fleet
        

        