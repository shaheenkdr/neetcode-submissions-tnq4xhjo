from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)


        for word in strs:

            f_map = [0] * 26

            base = ord('a')

            for char in word:
                f_map[ord(char) - base]+=1
            
            res[tuple(f_map)].append(word)
        
        return list(res.values())
