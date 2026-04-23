class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m,n = len(nums1) , len(nums2)

        total = m + n

        half = (total + 1) // 2

        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            num1_left = nums1[i-1] if i > 0 else float('-inf')
            num1_right = nums1[i] if i < m else float('inf')
            num2_left = nums2[j-1] if j > 0 else float('-inf')
            num2_right = nums2[j] if j < n else float('inf')

            if num1_left <= num2_right and num2_left <= num1_right:
                if total % 2:
                    return max(num1_left, num2_left)
                return (max(num1_left, num2_left) + min(num1_right, num2_right)) / 2
            
            elif num1_left > num2_right:
                hi = i - 1
            
            else:
                lo = i + 1

