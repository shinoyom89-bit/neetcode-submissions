class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concated=[]
        for i in range(2):
            for num in nums:
                concated.append(num)
        return concated
        