
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for index,temperature in enumerate(temperatures):
            while stack and temperature>stack[-1][1]:
                stack_index=stack.pop()[0] # 0 having the index here
                diff=index-stack_index
                res[stack_index]=diff
            stack.append([index,temperature])
        return res