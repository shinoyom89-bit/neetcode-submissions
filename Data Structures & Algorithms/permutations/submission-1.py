class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        current,result=[],[]
        def bfs():
            if len(current)==len(nums):
                result.append(current.copy())
                return
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                current.append(nums[i])
                bfs()
                current.pop()
        bfs()
        return result