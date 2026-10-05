class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left=0
        right=len(nums)-1
        min_val=None
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                min_val=nums[mid]
                right=mid
        min_val=min(nums[left],nums[right])
        return min_val