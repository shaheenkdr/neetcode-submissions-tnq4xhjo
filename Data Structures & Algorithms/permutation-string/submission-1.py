class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        fmap1 = [0] * 26

        fmap2 = [0] * 26

        n = len(s1)
        lx = 0

        for char in s1:
            fmap1[ord(char) - ord('a')] +=1

        
        for rx in range(len(s2)):
            fmap2[ord(s2[rx]) - ord('a')] +=1

            if (rx - lx + 1) > n:
                if fmap2[ord(s2[lx]) - ord('a')] != 0:
                    fmap2[ord(s2[lx]) - ord('a')] -=1

                lx+=1
            
            if (rx - lx + 1) == n and fmap1 == fmap2:
                return True

        

        return False
        