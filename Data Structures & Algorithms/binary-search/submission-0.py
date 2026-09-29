class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left <=right:
            mids=(left+right)//2
            if nums[mids]==target:
                return mids
            elif nums[mids]>target:
                right=mids-1
            elif nums[mids]<target:
                left=mids+1
        return -1