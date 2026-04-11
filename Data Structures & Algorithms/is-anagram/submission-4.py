class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        f_map = [0] * 26

        ref = [0] * 26

        for i in range(len(s)):

            f_map[ord(s[i]) - ord('a')]+=1
        
        for j in range(len(t)):
            f_map[ord(t[j]) - ord('a')]-=1
        

        return f_map == ref