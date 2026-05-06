class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 1:
            return 0


        lx = 0

        seen = {}

        max_l = -1

        for rx, char in enumerate(s):

            if char in seen and seen[char] >= lx:
                lx = seen[char] + 1
            
            seen[char] = rx

            max_l = max(max_l, rx - lx + 1)

        
        return max_l




        