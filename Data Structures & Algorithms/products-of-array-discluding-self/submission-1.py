class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        left = 1
        right = 1

        i = 0
        j = n - 1

        while i < n:
            res[i] *= left
            left *= nums[i]

            res[j] *= right
            right *= nums[j]

            i += 1
            j -= 1

        return res