class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashing = {}
        for n in nums:
            hashing[n] = hashing.get(n, 0) + 1

        for n, freq in hashing.items():
            if freq > 1:
                return True

        return False
