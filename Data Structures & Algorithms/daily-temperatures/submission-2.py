class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stack_ind=stack.pop()
                res[stack_index]=(i - stack_ind)
            stack.append([t,i])
        return res
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_index = stack.pop()[1]
                res[stack_index] = i - stack_index

            stack.append([t, i])

        return res