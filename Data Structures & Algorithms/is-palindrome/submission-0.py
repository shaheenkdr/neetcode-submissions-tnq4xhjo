class Solution:
    def isPalindrome(self, s: str) -> bool:

       
        y = []
        for char in s:
            if char.isalnum():
                y.append(char.lower())
        
        return y == y[::-1]
    

    


        
    