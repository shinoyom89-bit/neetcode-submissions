class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        long=1
        current=1
        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                current+=1
            else:
                current=1
            long=max(long,current)
        return long
















































# this one pass thte only first two test cases

#   if  len(nums)==1:
#             return 1
#         nums.sort()
#         nd=set()
#         for n in nums:
#             nd.add(n)
#         res=set()
#         i=0
#         while i < len(nums)-1:
#             diff=nums[i+1]-nums[i]
#             if diff==1:
#                 res.add(nums[i])
#                 res.add(nums[i+1])
#             i+=1
#         return len(res)

