class Solution:
    def isValid(self, s: str) -> bool:

        bpairs = {')':'(', '}':'{', ']':'['}

        stack = []

        for char in s:

            if char in bpairs:

                if stack and stack[-1] == bpairs[char]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(char)
        

        return True if not stack else False
        