class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def char_map(arr: str) -> List[int]:

            count = [0] * 26

            for char in arr: 

                count[ord(char) - ord('a')]+=1
            
            return count
        

        return char_map(s) == char_map(t)