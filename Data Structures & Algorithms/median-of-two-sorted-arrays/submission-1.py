import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pos1 = 0
        pos2 = 0
        total_len = len(nums1) + len(nums2)
        odd = total_len % 2 == 1
        res1 = None
        
        for i in range(math.floor(total_len / 2) + 1):
            # Check if nums1 is exhausted or if nums2 still has elements and current nums2 is smaller
            if pos1 < len(nums1) and (pos2 >= len(nums2) or nums1[pos1] < nums2[pos2]):
                val = nums1[pos1]
                pos1 += 1
            else:
                val = nums2[pos2]
                pos2 += 1
            
            if i == math.floor(total_len / 2) - 1:
                res1 = val
            if i == math.floor(total_len / 2):
                if odd:
                    return float(val)
                else:
                    return (res1 + val) / 2.0