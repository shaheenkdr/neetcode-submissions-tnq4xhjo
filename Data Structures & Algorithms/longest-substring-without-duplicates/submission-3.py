class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()

        lx = 0

        max_len = 0

        for rx in range(len(s)):

            while s[rx] in seen:
                seen.remove(s[lx])
                lx+=1

            seen.add(s[rx])

            max_len = max(max_len, rx - lx + 1 )
        

        return max_len

        