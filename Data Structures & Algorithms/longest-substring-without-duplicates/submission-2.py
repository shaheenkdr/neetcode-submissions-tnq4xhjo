class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_l = 0

        lx = 0

        seen = set()

        for rx in range(len(s)):

            while s[rx] in seen:
                seen.remove(s[lx])
                lx+=1
            
            seen.add(s[rx])

            max_l = max(max_l, rx - lx + 1)
        

        return max_l