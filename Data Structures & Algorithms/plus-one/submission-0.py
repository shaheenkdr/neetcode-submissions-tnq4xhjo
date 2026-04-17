class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = 0

        for num in digits:
            res = res * 10 + num
        
        res+=1

        return list(map(int,str(res)))
        