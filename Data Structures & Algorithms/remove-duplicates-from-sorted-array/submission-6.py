from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[l] = nums[i]
                l += 1
        return l  # ✅ return number of unique elements, not the slice

# Example:
nums = [1,1,2,3,4,5,5]
sol = Solution()
k = sol.removeDuplicates(nums)
print(k)        # Output: 5
print(nums[:k]) # Unique elements: [1,2,3,4,5]
