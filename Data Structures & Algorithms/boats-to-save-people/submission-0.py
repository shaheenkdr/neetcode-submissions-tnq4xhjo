class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        _bcount = 0 

        people.sort()

        lx , rx = 0, len(people) - 1
        while lx <= rx: 

            weight = people[lx] + people[rx]

            if weight <= limit:
                _bcount+=1
                lx+=1
                rx -=1
            
            else: 
                _bcount+=1
                rx-=1
        
        return _bcount


        