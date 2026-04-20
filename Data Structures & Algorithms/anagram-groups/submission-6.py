from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for word in strs:

            fmap = [0] * 26

            for char in word: 
                fmap[ord(char) - ord('a')]+=1
            
            res[tuple(fmap)].append(word)
        
        return list(res.values())