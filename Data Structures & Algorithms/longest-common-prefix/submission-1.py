class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        _main = strs[0]

        res = []

        for i,char in enumerate(_main):

            for word in range(1, len(strs)):
                if i >= len(strs[word]) or char!= strs[word][i]:
                    return "".join(res)
            res.append(char)
        

        return "".join(res)




    
        