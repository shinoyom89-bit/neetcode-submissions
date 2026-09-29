class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for index,number in enumerate(nums):
            if number==nums[index-1] and index>0:
                continue
            left=index+1
            right=len(nums)-1
            while left < right:
                three_sum=number+nums[left]+nums[right]
                if three_sum<0:
                    left+=1
                elif three_sum>0:
                    right-=1
                else:
                    res.append([number,nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1    
        return res