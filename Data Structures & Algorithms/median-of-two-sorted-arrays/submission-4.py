class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b=nums1,nums2
        if len(a)>len(b):
            a,b=b,a
        total=len(a)+len(b)
        half=(total+1)//2
        left,right=0,len(a)
        while left<=right:
            i=(left+right)//2
            j=half-i
            a_left=a[i-1] if i>0 else float("-infinity")
            a_right=a[i] if i<len(a) else float("infinity")
            b_left=b[j-1] if j>0 else float("-infinity")
            b_right=b[j] if j<len(b) else float("infinity")
            if a_left<=b_right and b_left<=a_right:
                if total%2==0:
                    return ( max(a_left,b_left)+min(a_right,b_right))/2
                else:
                    return max(a_left,b_left)
            elif a_left>b_right:
                right=i-1
            else:
                left=i+1
        
