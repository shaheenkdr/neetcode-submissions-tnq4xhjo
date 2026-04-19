class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        race = list(zip(position, speed))

        fleet = 0

        prev_time = 0

        for p,s in sorted(race, reverse = True):

            time = (target - p) / s

            if time > prev_time:
                fleet+=1
                prev_time = time
        
        return fleet