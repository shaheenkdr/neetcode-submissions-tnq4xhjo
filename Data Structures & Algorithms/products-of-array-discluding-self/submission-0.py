class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1

        prefix = []
        postfix = []

        for i in range(len(nums)):
            prod *= nums[i]
            prefix.append(prod)
        

        prod = 1
        for j in range(len(nums)-1, -1, -1):
            prod *= nums[j]
            postfix.append(prod)
        
        postfix.reverse()
        
        
        res = []

        l1,r1 = 0,0
        for i in range(len(nums)):

            l1 = prefix[i-1] if i > 0 else 1
            r1 = postfix[i+1] if i < len(nums) - 1 else 1
            res.append(l1 * r1)
        
        return res

            



        