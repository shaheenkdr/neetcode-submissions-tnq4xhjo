from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        c1 = Counter(s1)

        n = len(s1)

        lx = 0

        for rx in range(len(s2)):

            if (rx - lx + 1) > n:
                lx+=1
            
            if (rx - lx + 1) == n and c1 == Counter(s2[lx:rx+1]):
                return True



        return False
        