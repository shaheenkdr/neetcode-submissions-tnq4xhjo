class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n = len(arr)

        max_l = -1

        for x in reversed(range(n)):

            temp = arr[x]

            arr[x] = max_l 

            max_l = max(max_l, temp)
        

        return arr


