class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}

        lx = 0
        max_len = 0

        for right, char in enumerate(s):

            if char in seen and seen[char] >= lx:
                lx = seen[char] + 1
            
            seen[char] = right

            max_len = max(max_len, right - lx + 1)
        
        return max_len


        