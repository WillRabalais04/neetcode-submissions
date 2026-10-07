class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A,B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total_len = (len(A) + len(B)) 
        half_len = total_len // 2

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half_len - i - 2

            AL = A[i] if i >= 0 else float("-infinity")
            AR = A[i + 1] if (i + 1) < len(A) else float("infinity")
            BL = B[j] if j >= 0 else float("-infinity")
            BR = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if AL <= BR and BL <= AR:
                if total_len % 2:
                    return min(AR, BR)
                return (max(AL, BL) + min(AR, BR)) / 2
            elif AL > BR:
                r = i - 1
            else: 
                l = i + 1
                