class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}

        lx = 0
        max_l = 0

        for rx in range(len(s)):

            freq[s[rx]] = 1 + freq.get(s[rx], 0)

            while (rx - lx + 1) - max(freq.values()) > k:

                if freq.get(s[lx], 0) > 0:
                    freq[s[lx]]-=1
                
                else:
                    del freq[s[lx]]
                
                lx+=1
            
            max_l = max(max_l, rx - lx + 1)
        
        return max_l

