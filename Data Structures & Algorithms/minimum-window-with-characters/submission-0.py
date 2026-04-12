class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window, t_map = {}, {}

        for x in t:
            t_map[x] = t_map.get(x, 0) + 1
        
        res = [-1,-1]
        max_len = float("inf")

        have, needed  = 0, len(t_map)

        lx = 0

        for rx in range(len(s)):

            char = s[rx]

            window[char] = 1 + window.get(char, 0)

            if char in t_map and window[char] == t_map[char]:
                have+=1
            
            while have == needed:

                if (rx - lx + 1) < max_len:
                    res = [lx,rx]
                    max_len = (rx - lx + 1)

                window[s[lx]]-=1

                if s[lx] in t_map and window[s[lx]] < t_map[s[lx]]:
                    have -=1

                lx+=1
        
        lx, rx = res

        return s[lx:rx+1] if max_len != float("inf") else  ""



            



        