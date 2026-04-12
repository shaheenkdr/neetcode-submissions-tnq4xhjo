class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:


        lx = 0

        max_xp = 0
        xp = 0

        base = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]

        for rx in range(len(customers)):

            if grumpy[rx]:
                xp+=customers[rx]

            
            if (rx - lx + 1) > minutes:
                if grumpy[lx]:
                    xp-= customers[lx]
                
                lx+=1
            
            max_xp = max(max_xp, xp)
        
        return base + max_xp


            

        