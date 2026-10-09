class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        r = nums1 + nums2
        r.sort()

        n = len(r)
        mid = n // 2

        if n % 2 == 1:
            return r[mid]

        return (r[mid - 1] + r[mid]) / 2