class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        current,result=[],[]
        nums.sort()
        def bfs(idx):
            if idx==len(nums):
                result.append(current.copy())
                return
            current.append(nums[idx])
            bfs(idx+1)
            current.pop()
            while idx+1<len(nums) and nums[idx+1]==nums[idx]:
                idx+=1
            bfs(idx+1)
        bfs(0)
        return(result)