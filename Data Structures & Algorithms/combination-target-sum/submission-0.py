class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        current,result=[],[]
        def dfs(i,curr,total):
            if total==target:
                result.append(current.copy())
                return 
            elif i>=len(nums) or total>target:
                return
            current.append(nums[i])
            dfs(i,current,total+nums[i])
            current.pop()
            dfs(i+1,current,total)
        dfs(0,[],0)
        return result