class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        pt1,pt2 = 0, len(numbers) - 1


        while pt1 < pt2: 

            total = numbers[pt1] + numbers[pt2]

            if total == target:
                return [pt1+1,pt2+1]
            

            if total > target:
                pt2-=1
            else:
                pt1+=1

            
        