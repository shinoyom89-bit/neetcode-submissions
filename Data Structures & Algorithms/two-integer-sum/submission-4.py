class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,n in  enumerate(nums):
            diff=target-n
            if diff not in hash:
                hash[n]=i
            elif diff in hash:
                return [hash[diff],i]