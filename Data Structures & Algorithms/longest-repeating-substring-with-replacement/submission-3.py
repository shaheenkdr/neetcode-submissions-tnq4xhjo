class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        f_map = {}
        res = 0 
        lx = 0

        for rx in range(len(s)):

            f_map[s[rx]] = 1 + f_map.get(s[rx], 0)

            while (rx - lx + 1) - max(f_map.values()) > k:
                f_map[s[lx]]-=1
                lx+=1
            
            res = max(res, rx - lx + 1)
        
        return res


        