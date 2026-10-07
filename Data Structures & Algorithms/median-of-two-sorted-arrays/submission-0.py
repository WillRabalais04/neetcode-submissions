class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if not nums1 and not nums2:
            return 0.0
            
        merged = []
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        m = len(merged) // 2
        print(merged)
        if len(merged) % 2 == 0:
            return (merged[m - 1] + merged[m]) / 2
        else:
            return merged[m]

