
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                stackindex=stack.pop()[0]
                res[stackindex]=i-stackindex
            stack.append([i,t])
        return res
