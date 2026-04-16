class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = [] 

        for char in tokens:

            if char in ['+', '-', '*', '/']:

                b = int(stack.pop())
                a = int(stack.pop())

                if char == '+':
                    stack.append(a + b)
                
                elif char == '-':
                    stack.append(a - b)
                
                elif char == '*':
                    stack.append(a * b)
                
                else:
                    stack.append(int(a/b))
            
            else:
                stack.append(char)
        
        return int(stack[0])
        