class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sets=set()
        for n in nums:
            if n in sets:
                return n
            else:
                sets.add(n)
