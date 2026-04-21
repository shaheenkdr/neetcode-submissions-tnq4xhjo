class Solution:
    def findMin(self, nums: List[int]) -> int:

        lx, rx = 0, len(nums) - 1

        while lx < rx:

            mid = (lx + rx) // 2

            if nums[mid] > nums[rx]:
                lx = mid + 1
            else:
                rx = mid

        return nums[lx]        